a, b = map(int, input().split())
c = a + b

res = -1

if c >= 15 and b >= 8:
    res = 1
elif c >= 10 and b >= 3:
    res = 2
elif c >= 3:
    res = 3
else:
    res = 4

print(res)
