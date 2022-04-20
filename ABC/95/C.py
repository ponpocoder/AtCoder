a, b, c, x, y = map(int, input().split())

count_a = 0
count_b = 0
res = 0

if c < (a + b) / 2:
    while count_a < x and count_b < y:
        count_a += 0.5
        count_b += 0.5
        res += c

while count_a < x:
    if c < a / 2:
        count_a += 0.5
        res += c
    else:
        count_a += 1
        res += a

while count_b < y:
    if c < b / 2:
        count_b += 0.5
        res += c
    else:
        count_b += 1
        res += b

print(res)