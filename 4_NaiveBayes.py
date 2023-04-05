import re
from collections import defaultdict
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

class NaiveBayes:
    def __init__(self, classes: list):
        self.classes = classes
        self.vocab = set()
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_doc_counts = defaultdict(int)
        self.num_docs = 0
        
    def preprocess(self, text: str) -> list:
        text = re.sub(r'[^\w\s]', '', text).lower()
        stop_words = set(['a', 'an', 'the', 'in', 'on', 'at', 'of', 'to', 'for', 'by', 'with', 'from', 'and'])
        tokens = text.split()
        tokens = [token for token in tokens if token not in stop_words]
        return tokens

    def train(self, documents):
        for document, category in documents:
            tokens = self.preprocess(document)
            self.vocab.update(tokens)
            self.class_doc_counts[category] += 1
            self.num_docs += 1
            for word in tokens:
                self.class_word_counts[category][word] += 1
        
    def predict(self, document):
        tokens = self.preprocess(document)
        posteriors = {category: 0 for category in self.classes}
        for category in self.classes:
            prior = self.class_doc_counts[category] / self.num_docs
            posterior = prior
            for word in tokens:
                word_count = self.class_word_counts[category][word]
                total_count = sum(self.class_word_counts[category].values())
                conditional = word_count / total_count
                posterior *= conditional
            posteriors[category] = posterior
        return max(posteriors, key=posteriors.get)
    
docs = [
    ('The sky is blue', 'weather'), 
    ('The sun is bright', 'weather'),
    ('It is raining', 'weather'),
    ('The news is depressing', 'politics'),
    ('The election is coming up', 'politics'),
    ('The election has ended', 'politics'),
    ('The economy is doing good', 'economy'),
    ('He lost his job because of the economy', 'economy'),
    ('The economy is improving', 'economy'),
    ('The movie was great', 'entertainment'),
    ('I saw the movie at home', 'entertainment'),
    ('I liked the movie', 'entertainment'),
    ('I like to eat pizza', 'food'),
    ('I just ate lunch', 'food'),
    ('I eat rice once a day', 'food'),
    ('The game was exciting', 'sports'),
    ('The team played poorly', 'sports'),
    ('The players were tired after the match', 'sports')
]

nb = NaiveBayes(['weather', 'politics', 'economy', 'entertainment', 'food', 'sports'])
nb.train(docs)

phrase_1 = 'The movie was nice'
phrase_2 = 'The sun is bright'
phrase_3 = 'The economy is improving'
phrase_4 = 'I like to eat noodles'
phrase_5 = 'ELECTION is coming up'
phrase_6 = 'Did you watch the GAME last night'
category1 = nb.predict(phrase_1)
category2 = nb.predict(phrase_2)
category3 = nb.predict(phrase_3)
category4 = nb.predict(phrase_4)
category5 = nb.predict(phrase_5)
category6 = nb.predict(phrase_6)
print(f'The phrase "{phrase_1}" belongs to the category "{category1}"')
print(f'The phrase "{phrase_2}" belongs to the category "{category2}"')
print(f'The phrase "{phrase_3}" belongs to the category "{category3}"')
print(f'The phrase "{phrase_4}" belongs to the category "{category4}"')
print(f'The phrase "{phrase_5}" belongs to the category "{category5}"')
print(f'The phrase "{phrase_6}" belongs to the category "{category6}"')
true_vals = ['entertainment', 'weather', 'economy', 'food', 'politics', 'sports']
pred_vals = [category1, category2, category3, category4, category5, category6]
print(confusion_matrix(true_vals, pred_vals))
print(accuracy_score(true_vals, pred_vals))
print(classification_report(true_vals, pred_vals))