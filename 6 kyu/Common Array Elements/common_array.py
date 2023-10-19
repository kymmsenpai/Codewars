from collections import Counter

def common(a, b, c):
    aa = Counter(a)
    bb = Counter(b)
    cc = Counter(c)
    filtered = list(aa.keys() & bb.keys() & cc.keys())
    return sum([f * min(aa[f], bb[f], cc[f])  for f in filtered])