n = int(input())
res = 0

for _ in range(n):
    x, u = input().split()
    if u == "JPY":
        res += int(x)
    else:
        res += float(x) * 380000

print(res)
