a, b = map(int, input().split())

curr = 1
res = 0

while curr < b:
    curr += a - 1
    res += 1
print(res)