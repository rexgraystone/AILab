# 7. Write a Python program to implement Named Entity recognition.

import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words') # Uncomment these lines if the specified files aren't downloaded

paragraph = """Scarface is a 1983 American crime drama film directed by Brian De Palma and written by Oliver Stone. \
    Loosely based on the 1929 novel of the same name and serving as a loose remake of the 1932 film,\
    it tells the story of Cuban refugee Tony Montana (Al Pacino), \
    who arrives penniless in Miami during the Mariel boatlift and becomes a powerful and extremely homicidal drug lord.\
    The film co-stars Steven Bauer, Michelle Pfeiffer, Mary Elizabeth Mastrantonio and Robert Loggia.\
    De Palma dedicated this version of Scarface to the memories of Howard Hawks and Ben Hecht, \
    the writers of the original film."""

for sentence in nltk.sent_tokenize(paragraph):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
        if hasattr(chunk, 'label'):
            print(f"{' '.join(c[0] for c in chunk):<35} {chunk.label()}")