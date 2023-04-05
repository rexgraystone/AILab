import re
from collections import defaultdict

class NaiveBayes:
    def __init__(self, classes):
        self.classes = classes
        self.vocab = set()
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_doc_counts = defaultdict(int)
        self.num_docs = 0
        
    def preprocess(self, text):
        # Remove punctuations and convert to lowercase
        text = re.sub(r'[^\w\s]', '', text).lower()
        # Remove stop words
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
    
docs = [('The sky is blue', 'weather'), 
        ('The sun is bright', 'weather'),
        ('The news is depressing', 'politics'),
        ('The economy is improving', 'economy'),
        ('The movie was great', 'entertainment'),
        ('I love pizza', 'food'),
        ('The game was exciting', 'sports'),
        ('The team played poorly', 'sports'),
        ('The election is coming up', 'politics')]

nb = NaiveBayes(['weather', 'politics', 'economy', 'entertainment', 'food', 'sports'])
nb.train(docs)

new_doc1 = 'ELECTION is coming up'
new_doc2 = 'The sun is bright'
new_doc3 = 'The economy is improving'
category1 = nb.predict(new_doc1)
category2 = nb.predict(new_doc2)
category3 = nb.predict(new_doc3)
print(f'The document "{new_doc1}" belongs to the category "{category1}"')
print(f'The document "{new_doc2}" belongs to the category "{category2}"')
print(f'The document "{new_doc3}" belongs to the category "{category3}"')