n = int(input())
t = input()
dir = [1, 0]
res = [0, 0]
for c in t:
    if c == "S":
        res[0] += dir[0]
        res[1] += dir[1]
    else:
        x, y = dir
        dir[0] = y if y != 0 else 0
        dir[1] = -x

print(*res)