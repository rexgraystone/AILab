import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

file_path = '6_RestaurantReviews.tsv'
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


