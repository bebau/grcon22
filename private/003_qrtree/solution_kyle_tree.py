#!/usr/bin/env python3
'''
Decision Tree Classifier

98% accuracy with 2000 training samples
'''
import numpy as np
import pandas as pd
from sklearn import tree
from PIL import Image


BLAH = '../../public/003_qrtree/'
train_data = pd.read_csv(BLAH+'train_data.csv', index_col=False)
train_x = train_data[['0', '1', '2', '3', '4', '5', '6', '7']].values
train_y = train_data.y.values
test_x = pd.read_csv(BLAH+'test_x_data.csv', index_col=False).values

classifier = tree.DecisionTreeClassifier()
classifier.fit(train_x, train_y)

test_y = classifier.predict(test_x)
test_y_df = pd.DataFrame({'y': test_y})
#test_y_df.to_csv('/tmp/test_y_data.csv')
#print('verify against /tmp/test_y_data.csv')

img = Image.fromarray(test_y.reshape(107, 97).astype(np.uint8)*255, mode='L').convert('1')
img.save('qr_decode.png')

test_y_true = pd.read_csv('test_y_data.csv', index_col=False).values.T[0]

accuracy = (test_y == test_y_true).sum() / (107*97)
print(f'accuracy={accuracy:.4%}')

print('done')