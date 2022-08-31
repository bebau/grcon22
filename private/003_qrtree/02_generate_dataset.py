#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image

np.random.seed(seed=0xDEADBEEF+55000)

feature_count = 8
# Row counts
total_count = 50000
train_count = 1999

X = np.random.randn(total_count, feature_count)

positive_examples = (
    ((X[:, 0] > -0.5) & (X[:, 1] > -0.31) & (X[:, 2] > -0.2) & (X[:, 1] < 0.5))
    | ((X[:, 7] > -0.25) & (X[:, 4] > 0.0) & (X[:, 5] > 0.2) & (X[:, 7] < 0.7))
) | ((X[:, 3] < -0.1))

df = pd.DataFrame(X)
df['y'] = positive_examples * 1

# save training data
training = df.loc[:train_count] # first are training


# construct test data
with Image.open('qr_padded.png') as img:
    solution = np.array(img).ravel()

# read the image and sort our solutions into the test data
test_df = pd.DataFrame(columns=df.columns)
idx = 0
for key in solution:
    while df['y'][train_count+idx] != key:
        idx += 1
        if idx > total_count:
            raise ValueError('could not construct test dataset; increase total_count')
    test_df = test_df.append(df.loc[train_count+idx], ignore_index=True)
    idx += 1

print('rows required during gen:', idx)

test_x = test_df.loc[:, range(feature_count)]
test_y = test_df.loc[:, 'y']


# construct example submission
# trash_y = test_y.copy()
# trash_y[:] = np.zeros(total_count - train_count, dtype=int)

dir_private = Path.cwd()
puzzle_name = dir_private.name
dir_public = dir_private.parent.parent / 'public' / puzzle_name
training.to_csv(dir_public / 'train_data.csv', index=False)



test_x.to_csv(dir_public / 'test_x_data.csv', index=False)
# trash_y.to_csv(dir_public / 'test_y_data.csv', index=False)
test_y.to_csv(dir_private / 'test_y_data.csv', index=False)

print('done')
