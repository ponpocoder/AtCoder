from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)

for v in a:
    dic[v] += 1

s = 0
for v in dic.values():
    if v >= 2:
        s += v * (v-1) // 2

for k in range(n):
    curr = s
    v = dic[a[k]]
    curr -= v*(v-1) // 2
    v -= 1
    curr += v*(v-1) // 2
    print(curr)