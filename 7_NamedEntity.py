# 7. Write a Python program to implement Named Entity recognition.

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words') # Uncomment these lines if the specified files aren't downloaded

sentence = """Python is an interpreted, high-level and general-purpose programming language"
       "Pythons design philosophy emphasizes code readability with"
       "its notable use of significant indentation."
       "Its language constructs and object-oriented approach aim to"
       "help programmers write clear and"
       "logical code for small and large-scale projects"""

for sent in nltk.sent_tokenize(sentence):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(f"{' '.join(c[0] for c in chunk):<35} {chunk.label()}")