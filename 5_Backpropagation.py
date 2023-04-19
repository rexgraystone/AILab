# 5. Write a Python program to implement the finite words classification system using backpropagation algorithm.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score

data = pd.read_csv('Datasets/5_FiniteWords.csv', names=['Message', 'Label'])
print("The Total instances in the Dataset: ", data.shape[0])
print(data)
data['labelnum'] = data.Label.map({'pos': 1, 'neg': 0})
print(data)
X = data["Message"]
y = data.labelnum
X_train, X_test, y_train, y_test = train_test_split(X, y)
count_vect = CountVectorizer()
X_train_dims = count_vect.fit_transform(X_train)
X_test_dims = count_vect.transform(X_test)
model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
model.fit(X_train_dims, y_train)
prediction = model.predict(X_test_dims)
print('********Accuracy Metrics*********')
print(f'Accuracy: {accuracy_score(y_test, prediction)}')
print(f'Recall: {recall_score(y_test, prediction)}')
print(f'Precision: {precision_score(y_test, prediction)}')
print(f'Confusion Matrix : \n{confusion_matrix(y_test, prediction)}')
print(10*"-")

test_stmt = [input("Enter any statement to predict: ")]
test_dims = count_vect.transform(test_stmt)
pred = model.predict(test_dims)
for stmt, lbl in zip(test_stmt, pred):
    if lbl == 1:
        print("Statement is Positive")
    else:
        print("Statement is Negative")