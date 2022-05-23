from collections import defaultdict

n = int(input())
s = []
for _ in range(n):
    s.append(input())

res = 100000
for i in range(10):
    curr = 0
    dic = defaultdict(int)
    for j in range(n):
        for k in range(10):
            if s[j][k] == str(i):
                dic[k] += 1
                break
            
    for k, v in dic.items():
        curr = max(curr, k + 10 * (v - 1))
    res = min(curr, res)

print(res)
