from collections import defaultdict
from math import ceil

s = input()
dic = defaultdict(int)

for c in s:
    dic[c] += 1

curr = 0
for v in dic.values():
    curr = max(curr, v)

if curr >= ceil(len(s) / 3) + 1:
    print("NO")
else:
    print("YES")