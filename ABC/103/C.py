n = int(input())
a = list(map(int, input().split()))

res = 0
for v in a:
    res += v - 1

print(res)
