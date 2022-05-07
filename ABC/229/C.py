n, w = map(int, input().split())

inputs = [list(map(int, input().split())) for _ in range(n)]
inputs.sort(reverse=True)
total = 0
res = 0

for d, weight in inputs:
    diff = w - total
    if diff > weight:
        res += d * weight
        total += weight
    else:
        res += d * diff
        break

print(res)