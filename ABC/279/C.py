from collections import defaultdict

h, w = map(int, input().split())
s = [[] for _ in range(w)]
t = [[] for _ in range(w)]

for _ in range(h):
    v = list(input())
    for i, c in enumerate(v):
        s[i].append(c)

for _ in range(h):
    v = list(input())
    for i, c in enumerate(v):
        t[i].append(c)

ss = defaultdict(int)
tt = defaultdict(int)
for v in s:
    ss["".join(v)] += 1

for v in t:
    tt["".join(v)] += 1
for key in ss.keys():
    if ss[key] != tt[key]:
        print("No")
        exit()

print("Yes")
