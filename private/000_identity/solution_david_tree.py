#!/usr/bin/env python3
'''
Decision Tree Classifier

91% accuracy with ~2500 training samples
'''
import numpy as np
import pandas as pd

from sklearn import tree

# get data
BLAH = '../../public/000_identity/'
train_x = pd.read_csv(BLAH+'train_x_data.csv', index_col=False)
test_x = pd.read_csv(BLAH+'test_x_data.csv', index_col=False)
train_y = pd.read_csv(BLAH+'train_y_data.csv', index_col=False)
test_y = pd.read_csv('test_y_data.csv', index_col=False)

# train classifier
classifier = tree.DecisionTreeClassifier()
classifier.fit(train_x, train_y)
predictions = classifier.predict(test_x)

accuracy = (predictions == np.squeeze(test_y)).sum() / len(predictions)
print(f'tree accuracy = {accuracy:.4%}')


# Now predict on the identity data
identity_x = pd.read_csv(BLAH+'identity_x.csv', index_col=False)
identity_y = classifier.predict(identity_x)

print(identity_y)

print('done')