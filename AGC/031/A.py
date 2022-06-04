from collections import defaultdict

n = int(input())
s = input()
mod = 10**9 + 7

dic = defaultdict(int)

for c in s:
    dic[c] += 1

res = 1
for v in dic.values():
    res *= (v+1)

res -= 1
print(res%mod)