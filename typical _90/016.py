n = int(input())
a, b, c = map(int, input().split())

x = 10000
res = 10000
for i in range(x):
    for j in range(x-i):
        curr = a*i + b*j
        if curr > n or (n-curr) % c != 0:
            continue
        res = min(res, (n-curr)//c+i+j)

print(res)
