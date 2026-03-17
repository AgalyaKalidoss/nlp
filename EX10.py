import nltk
from nltk.wsd import lesk
from nltk import word_tokenize, pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
sentence = "He went to the bank to deposit money"
word = "bank"
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)
sense = lesk(tokens, word)
print("Word:", word)
if sense:
    print("Best Sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")