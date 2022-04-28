import sys
from collections import defaultdict

n = int(input())
names = defaultdict(int)
s, t = [], []
for _ in range(n):
    a, b = map(str, input().split())
    s.append(a)
    t.append(b)
    names[a] += 1
    names[b] += 1

for i in range(n):
    names[s[i]] -= 1
    names[t[i]] -= 1
    if names[s[i]] > 0 and names[t[i]] > 0:
        print("No")
        sys.exit()
    names[s[i]] += 1
    names[t[i]] += 1
print("Yes")