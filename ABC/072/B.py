from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dic = defaultdict(int)

for v in a:
    dic[v-1] += 1
    dic[v] += 1
    dic[v+1] += 1

res = 0
for i, v in dic.items():
    res = max(res, v)

print(res)
