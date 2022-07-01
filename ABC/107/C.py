n, k = map(int, input().split())
x = list(map(int, input().split()))

res = float("inf")
for i in range(n-k+1):
    l = x[i]
    r = x[i + k - 1]
    curr = min(abs(l) + abs(l-r), abs(r) + abs(l - r))
    res = min(res, curr)

print(res)