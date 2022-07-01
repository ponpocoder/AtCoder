n = int(input())
c = list(map(int, input().split()))

mn = n
for v in c:
    mn = min(mn, v)

k = n // mn
res = ""
while k:
    for i in range(8, -1, -1):
        if n - c[i] >= mn*(k - 1):
            res += str(i+1)
            n -= c[i]
            break
    k -= 1

print(res)