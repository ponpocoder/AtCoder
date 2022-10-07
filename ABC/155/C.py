from collections import defaultdict

n = int(input())
dic = defaultdict(int)

mx = 0
for _ in range(n):
    s = input()
    dic[s] += 1
    mx = max(mx, dic[s])

res = []
for key, value in dic.items():
    if value == mx:
        res.append(key)

res.sort()
for v in res:
    print(v)



