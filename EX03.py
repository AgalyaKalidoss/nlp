import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('omw-1.4')

def get_wordnet_pos(word):
    tag = pos_tag([word])[0][1][0].upper()
    if tag == 'J':
        return wordnet.ADJ
    elif tag == 'V':
        return wordnet.VERB
    elif tag == 'N':
        return wordnet.NOUN
    elif tag == 'R':
        return wordnet.ADV
    else:
        return wordnet.NOUN

text = "The cats are running faster and ate the mice in the houses"

tokens = word_tokenize(text)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

processed_words = []

for word in tokens:
    word = word.lower()
    if word.isalpha() and word not in stop_words:
        pos = get_wordnet_pos(word)
        lemma = lemmatizer.lemmatize(word, pos)
        processed_words.append(lemma)

print("Original Text:")
print(text)

print("\nAfter Stopword Removal + Lemmatization:")
print(processed_words)

print("\nFinal Processed Sentence:")
print(" ".join(processed_words))
