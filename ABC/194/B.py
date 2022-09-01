n = int(input())
a = []
b = []

res = float("inf")

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(n):
    for j in range(n):
        if i == j:
            curr = a[i] + b[j]
        else:
            curr = max(a[i], b[j])

        res = min(res, curr)
print(res)
