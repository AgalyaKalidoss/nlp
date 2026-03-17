import math
w1, w2 = "night", "nacht"
c = set(w1 + w2)
v1 = [w1.count(x) for x in c]
v2 = [w2.count(x) for x in c]
cosine = sum(x*y for x,y in zip(v1,v2)) / (
    math.sqrt(sum(x*x for x in v1)) *
    math.sqrt(sum(y*y for y in v2))
)
print("Cosine Similarity:", cosine)