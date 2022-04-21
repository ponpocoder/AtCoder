from itertools import permutations
n = int(input())
pairs = []

for _ in range(n):
    x, y = map(int, input().split())
    pairs.append((x, y))

perms = list(permutations(list(range(n))))
res = 0
for perm in perms:
    l = list(perm)
    for i in range(n - 1):
        x = pairs[l[i]][0] - pairs[l[i + 1]][0]
        y = pairs[l[i]][1] - pairs[l[i + 1]][1]
        dist = (x ** 2 + y ** 2) ** 0.5
        res += dist

print(res / len(perms))
