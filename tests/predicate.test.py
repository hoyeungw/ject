from functools import reduce

from ject import oneself





def fa(x: str): return x.find('a') >= 0


def fb(x: str): return x.find('b') >= 0


def fc(x: str): return x.find('c') >= 0


intersected = intersect(fa, fb, fc)
unioned = union(fa, fb, fc)
candidates = [
    'paco robanne',
    'giorgio armani',
    'louis vuitton'
]

for word in candidates:
    print(word, intersected(word), unioned(word))
