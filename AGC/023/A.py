from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
s = [0] * (n+1)
d = defaultdict(int)
d[0] += 1

for i in range(1, n+1):
    s[i] = a[i-1] + s[i-1]
    d[s[i]] += 1
res = 0
for v in d.values():
    res += v * (v-1) // 2

print(res)