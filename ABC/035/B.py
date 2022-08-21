s = input()
t = int(input())

cnt = 0
x, y = 0, 0

for c in s:
    if c == "U":
        y += 1
    elif c == "D":
        y -= 1
    elif c == "L":
        x += 1
    elif c == "R":
        x -= 1
    else:
        cnt += 1

x = abs(x)
y = abs(y)

res = x + y
if t == 1:
    res += cnt
else:
    if cnt <= res:
        res -= cnt
    else:
        cnt -= res
        if cnt % 2:
            res = 1
        else:
            res = 0

print(res)
