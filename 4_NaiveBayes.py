# 4. Write a Python program to omplement naïve bayes theorem to classify the English text.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

X_train = ['I love playing sports', 'Politics is my passion', 'Sports are fun', 'Politics is boring']
y_train = ['sports', 'politics', 'sports', 'politics']
vectorizer = CountVectorizer(stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

X_test = ['I enjoy watching sports on TV', 'Politics is important for our country', 'i love politics']
X_test_counts = vectorizer.transform(X_test)
y_pred = model.predict(X_test_counts)

output = []
for index, i in enumerate(range(len(X_test))):
    output.append([X_test[i], y_pred[i]])
    print(output[index])