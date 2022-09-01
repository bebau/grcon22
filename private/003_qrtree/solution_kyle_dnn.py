#!/usr/bin/env python3
'''
Tried to implement the smallest possible fully connected approach; clearly overkill.

This solution works okay but might not have enough training data.
Got 957/1000 if allow maximum overfit.
Get 929/1000 when using 90/10 split.
'''
import numpy as np
import pandas as pd
from PIL import Image

import torch
import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint

# get data
BLAH = '../../public/003_qrtree/'
train_data = pd.read_csv(BLAH+'train_data.csv', index_col=False)
train_x = train_data[['0', '1', '2', '3', '4', '5', '6', '7']].values
train_y = train_data.y.values
test_x = pd.read_csv(BLAH+'test_x_data.csv', index_col=False).values

# classifier
raw_dataset = torch.utils.data.TensorDataset(torch.tensor(train_x, dtype=torch.float), torch.tensor(train_y, dtype=torch.float))
# 90/10 split
train_set, val_set = torch.utils.data.random_split(raw_dataset, [int(len(raw_dataset)*.9), int(len(raw_dataset)*.1)], generator=torch.Generator().manual_seed(0xDEADBEEF))

train_loader = torch.utils.data.DataLoader(train_set, batch_size=100, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_set, batch_size=100)
test_dataset = torch.utils.data.TensorDataset(torch.tensor(test_x, dtype=torch.float))

class Overkill(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.l0 = torch.nn.Linear(in_features=8, out_features=32)
        self.l1 = torch.nn.Linear(in_features=32, out_features=32)
        self.l3 = torch.nn.Linear(in_features=32, out_features=1)
        self.silu = torch.nn.SiLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.criterion = torch.nn.BCELoss()

    def forward(self, x):
        x = self.silu(self.l0(x))
        x = self.silu(self.l1(x))
        x = self.sigmoid(self.l3(x))
        return x

    def step(self, batch, batch_idx):
        x, y = batch
        x_hat = self.forward(x)
        loss = self.criterion(x_hat, y.unsqueeze(1))
        return loss

    def training_step(self, batch, batch_idx):
        return self.step(batch, batch_idx)

    def validation_step(self, batch, batch_idx):
        loss = self.step(batch, batch_idx)
        self.log('val_loss', loss)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=1e-3)

model = Overkill()
early = EarlyStopping(monitor='val_loss', mode='min', patience=50)
checkpoint = ModelCheckpoint(
    filename=f'overkill'+'-{epoch:05d}-{val_loss:.9f}', mode='min', dirpath='/tmp/',  monitor='val_loss')
trainer = pl.Trainer(callbacks=[early, checkpoint], max_epochs=1000)

trainer.fit(model, train_loader, val_loader)
print(f'rewind to best checkpoint {checkpoint.best_model_path}')
rewind = torch.load(checkpoint.best_model_path)
model.load_state_dict(rewind['state_dict'])
model.eval()

test_y = model(torch.tensor(test_x, dtype=torch.float)).round().detach().numpy().T[0]
# end classifier

# test_y_df = pd.DataFrame({'y': test_y})
#test_y_df.to_csv('/tmp/test_y_data.csv')
#print('verify against /tmp/test_y_data.csv')

img = Image.fromarray(test_y.reshape(107, 97).astype(np.uint8)*255, mode='L').convert('1')
img.save('qr_decode_dnn.png')

test_y_true = pd.read_csv('test_y_data.csv', index_col=False).values.T[0]
accuracy = (test_y == test_y_true).sum() / (107*97)
print(f'dnn accuracy = {accuracy:.4%}')

print('done')