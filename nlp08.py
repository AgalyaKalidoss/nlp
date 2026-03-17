def chunk(sentence):
    words = sentence.split()
    print("Words are :",words)
    for i in range(len(words)-1):
        if words[i].lower() in ['a','an','the']:
            print("NP ->", words[i], words[i+1])

sentence = "A bird in the hand is worth two in the bush."
chunk(sentence)

# --- added code for draw() ---
import nltk
from nltk.tree import Tree

words = sentence.split()
chunks = []

for i in range(len(words)-1):
    if words[i].lower() in ['a','an','the']:
        chunks.append(Tree('NP', [words[i], words[i+1]]))
    else:
        chunks.append(words[i])

chunks.append(words[-1])

tree = Tree('S', chunks)
tree.draw()