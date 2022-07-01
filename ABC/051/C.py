sx, sy, tx, ty = map(int, input().split())
res = []
dx = tx - sx
dy = ty - sy

for i in range(dx):
    res.append("R")
for i in range(dy):
    res.append("U")
for i in range(dx):
    res.append("L")
for i in range(dy):
    res.append("D")
res.append("D")
for i in range(dx+1):
    res.append("R")
for i in range(dy+1):
    res.append("U")
res.append("L")
res.append("U")
for i in range(dx+1):
    res.append("L")
for i in range(dy+1):
    res.append("D")
res.append("R")

print("".join(res))