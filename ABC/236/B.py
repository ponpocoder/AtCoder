n = int(input())
a = list(map(int, input().split()))

res = 0

for v in a:
    res ^= v

print(res)