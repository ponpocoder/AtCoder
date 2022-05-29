n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
res = sum(s)

if res % 10 == 0:
    i = 0
    while i < n and s[i] % 10 == 0:
        i += 1
    if i == n:
        print(0)
    else:
        print(res - s[i])
else:
    print(res)