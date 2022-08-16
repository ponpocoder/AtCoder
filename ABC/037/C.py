n, k = map(int, input().split())
a = list(map(int, input().split()))

res = 0
curr = sum(a[:k])
for i in range(n-k):
    res += curr
    curr = curr - a[i] + a[i+k]

res += curr

print(res)
