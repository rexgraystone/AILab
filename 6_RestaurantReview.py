# 6. Implement a model to correctly identify the sentiments of the user reviews for restaurants.

import numpy as np
import pandas as pd
# import nltk
# nltk.download('stopwords') # Uncomment these lines if you haven't downloaded 'stopwords'
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'Datasets/6_RestaurantReviews.tsv'
df = pd.read_csv(file_path, sep='\t', header=0)

corpus = []
for i in range(0,1000):
    review = re.sub(pattern='[^a-zA-Z]',repl=' ', string=df['Review'][i])
    review = review.lower()
    review_words = review.split()
    review_words = [word for word in review_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review_words]
    review = ' '.join(review)
    corpus.append(review)

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = df.iloc[:, 1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print("---- Scores ----")
print(f"Accuracy score is: {round(accuracy*100, 2)}%")
print(f"Precision score is: {round(precision,2)}")
print(f"Recall score is: {round(recall,2)}.")

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize = (10,6))
sns.heatmap(cm, annot=True, cmap="YlGnBu", xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.xlabel('Predicted values')
plt.ylabel('Actual values')
plt.show()

best_accuracy = 0.0
alpha_val = 0.0
for i in np.arange(0.1,1.1,0.1):
  temp_classifier = MultinomialNB(alpha=i)
  temp_classifier.fit(X_train, y_train)
  temp_y_pred = temp_classifier.predict(X_test)
  score = accuracy_score(y_test, temp_y_pred)
  print(f"Accuracy score for alpha={round(i, 1)} is: {round(score*100, 2)}%")
  if score > best_accuracy:
    best_accuracy = score
    alpha_val = i
print('--------------------------------------------')
print(f'The best accuracy is {round(best_accuracy*100, 2)}% with alpha value as {round(alpha_val, 1)}')

classifier = MultinomialNB(alpha=0.2)
classifier.fit(X_train, y_train)

def predict_sentiment(sample_review):
    sample_review = re.sub(pattern='[^a-zA-Z]',repl=' ', string = sample_review)
    sample_review = sample_review.lower()
    sample_review_words = sample_review.split()
    sample_review_words = [word for word in sample_review_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    final_review = [ps.stem(word) for word in sample_review_words]
    final_review = ' '.join(final_review)
    temp = cv.transform([final_review]).toarray()
    return classifier.predict(temp)

sample_review = input('Enter a sample review: ')

if predict_sentiment(sample_review):
    print('This is a POSITIVE review!')
else:
    print('This is a NEGATIVE review!')