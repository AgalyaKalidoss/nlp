def pos_tag(sentence):
    for word in sentence.split():
        w = word.lower()

        if w in ['is','am','are','was','were']:
            tag = 'VB'
        elif w.endswith('ing'):
            tag = 'VBG'
        elif w in ['a','an','the']:
            tag = 'DT'
        else:
            tag = 'NN'
        print(word, "->", tag)
sentence = "Artificial Intelligence is transforming education"
pos_tag(sentence)