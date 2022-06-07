from collections import defaultdict

n = int(input())
s = [sorted(list(input())) for _ in range(n)]

for i in range(n):
    s[i] = "".join(s[i])
    
dic = defaultdict(int)

res = 0
for v in s:
    dic[v] += 1
for v in dic.values():
    res += v * (v - 1) // 2

print(res) 