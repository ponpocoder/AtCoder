l, r = map(int, input().split())
mod = 2019
res = float("inf")

for i in range(l, l + 2019):
    if i > r:
        break
    for j in range(i + 1, l + 2019):
        if j > r:
            break
        curr = i * j % mod
        res = min(curr, res)

print(res)

