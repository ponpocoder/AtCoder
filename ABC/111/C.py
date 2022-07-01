from collections import defaultdict

n = int(input())
v = list(map(int, input().split()))

v1 = [v[i] for i in range(0, n, 2)]
v2 = [v[i] for i in range(1, n, 2)]

dic1 = defaultdict(int)
dic2 = defaultdict(int)

for v in v1:
    dic1[v] += 1

for v in v2:
    dic2[v] += 1

x = []
y = []

for key, value in dic1.items():
    x.append((key, value))
for key, value in dic2.items():
    y.append((key, value))

x.sort(key=lambda x:x[1], reverse = True)
y.sort(key=lambda x:x[1], reverse = True)

if x[0][0] != y[0][0]:
    res = n - x[0][1] - y[0][1]
else:
    if x[0][1] > y[0][1]:
        res = n - x[0][1] - y[1][1] if len(y) > 1 else n // 2
    elif x[0][1] == y[0][1]:
        res = n - x[0][1] - max(x[1][1] if len(x) > 1 else 0, y[1][1] if len(y) > 1 else 0)
    else:
        res = n - y[0][1] - x[1][1] if len(x) > 1 else n // 2
        

print(res)