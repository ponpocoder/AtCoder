n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7
p, q = 0, 0

for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            p += 1

for i in range(n):
    for j in range(n):
        if a[i] > a[j]:
            q += 1

res = p * k + q * k * (k - 1) // 2
print(res%mod)