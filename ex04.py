from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize
import string

stemmer = PorterStemmer()

text = "Preprocessing includes tokenization, normalization, and stemming."

text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

words = wordpunct_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in words]

print("Original words:", words)
print("Stemmed words:", stemmed_words)