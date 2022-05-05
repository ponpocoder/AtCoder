from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * n
curr = 0

for i, v in enumerate(a):
    curr += v
    s[i] += curr

res = 0

dic = defaultdict(int)
dic[0] += 1

for i in range(n):
    diff = s[i] - k
    res += dic[diff]
    dic[s[i]] += 1

print(res)
