from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

dic = defaultdict(int)
dic[0] = 1

curr = 0
res = 0
for i, v in enumerate(a):
    curr += v
    curr %= m
    res += dic[curr]
    dic[curr] += 1
print(res)
