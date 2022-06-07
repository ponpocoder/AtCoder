n = int(input())
a, b = [], []

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

d = []

res = 0

for i in reversed(range(n)):
    a[i] = (res+a[i]) % b[i]
    if a[i] != 0:
        res += b[i] - a[i]  

print(res)