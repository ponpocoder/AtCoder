a, b, k = map(int, input().split())
res = 0
while a < b:
    a *= k
    res += 1

print(res)