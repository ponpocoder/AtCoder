n = int(input())
x = list(map(int, input().split()))

res = 1001001001

for i in range(1, 101):
    curr = 0
    for j in range(n):
        curr += (x[j]-i)**2

    res = min(res, curr)

print(res)
