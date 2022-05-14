n = int(input())
s = set()
idx = []
scores = []
for i in range(n):
    x, y = input().split()
    if x not in s:
        s.add(x)
        idx.append(i)
    scores.append(int(y))

curr = 0
res = 0
for i in idx:
    if scores[i] > curr:
        curr = scores[i]
        res = i

print(res+1)