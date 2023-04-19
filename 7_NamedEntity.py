import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

sentence = """The Kashmir Files is a 2022 Indian Hindi-language drama film, \
written and directed by Vivek Agnihotri. Produced by Zee Studios, \
the film is based on the exodus of Kashmiri Pandits during the Kashmir Insurgency, \
which it portrays as a genocide. \
It stars Anupam Kher, Darshan Kumar, Pallavi Joshi and Mithun Chakraborty."""

for sent in nltk.sent_tokenize(sentence):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(f"{' '.join(c[0] for c in chunk):<35} {chunk.label()}")

