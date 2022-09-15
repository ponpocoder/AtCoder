n = int(input())

s = set()
for i in range(1, n+1):
    if i * i > n:
        break
    if n % i == 0:
        s.add(n//i)
        s.add(i)

res = list(s)
res.sort()
for v in res:
    print(v)
