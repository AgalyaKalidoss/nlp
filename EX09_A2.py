w1, w2 = "night", "nacht"
jaccard = len(set(w1)&set(w2)) / len(set(w1)|set(w2))
print("Jaccard Similarity:", jaccard)