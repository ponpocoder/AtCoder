n = int(input())
a = list(map(int, input().split()))

curr = 0
for v in a:
    curr += v
ave = curr // n
ave2 = ave + 1

res = 0
res2 = 0

for v in a:
    res += (ave - v) ** 2
    res2 += (ave2 - v) ** 2

print(min(res, res2))