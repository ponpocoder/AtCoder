from collections import defaultdict

s = input()
n = len(s)
m = 2019

x = 1
curr = 0
res = 0
dic = defaultdict(int)
dic[0] += 1
for i in range(n-1, -1, -1):
    curr += int(s[i]) * x
    curr %= m
    res += dic[curr]
    dic[curr] += 1
    x = x * 10 % m

print(res)
