from collections import defaultdict

n = int(input())

curr = defaultdict(int)
s = input()

for c in s:
    curr[c] += 1

for _ in range(n-1):
    dic = defaultdict(int)
    s = input()
    for c in s:
        dic[c] += 1
    
    for i in curr.keys():
        curr[i] = min(curr[i], dic[i])

a = []
for i in curr.keys():
    a.append(i)

a.sort()

res = ""

for v in a:
    res += v * curr[v]

print(res)