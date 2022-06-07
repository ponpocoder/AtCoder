a, b, x = map(int, input().split())

rem = a % x
if rem:
    a = a + x - rem
rem = b % x
b -= rem
res = (b - a) // x
if b % x == 0:
    res += 1

print(res)