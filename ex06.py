from collections import defaultdict
corpus = ["hello welcome", "to kcet"]
bigram, unigram, vocab = defaultdict(int), defaultdict(int), set()
for s in corpus:
    w = s.split()
    vocab.update(w)
    for i, word in enumerate(w):
        unigram[word] += 1
        if i < len(w) - 1:
            bigram[(w[i], w[i+1])] += 1
V = len(vocab)
pair = ("love", "python")
prob = (bigram[pair] + 1) / (unigram[pair[0]] + V)
print(f"Corpus: {corpus}")
print(f"Probability of {pair}: {round(prob, 4)}")