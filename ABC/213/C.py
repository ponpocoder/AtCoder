from collections import defaultdict

h, w, n = map(int, input().split())
a = set()
b = set()
ab = []
for _ in range(n):
    x, y = map(int, input().split())
    a.add(x)
    b.add(y)
    ab.append((x, y))

sortedA = sorted(list(a))
sortedB = sorted(list(b))

dictA = defaultdict(int)
dictB = defaultdict(int)

for i, v in enumerate(sortedA):
    dictA[v] = i + 1

for i, v in enumerate(sortedB):
    dictB[v] = i + 1

for i in range(n):
    print(dictA[ab[i][0]], dictB[ab[i][1]])