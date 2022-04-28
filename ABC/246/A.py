from collections import defaultdict
xDic = defaultdict(int) 
yDic = defaultdict(int) 

for _ in range(3):
    x, y = map(int, input().split())
    xDic[x] += 1
    yDic[y] += 1

resX = 0
resY = 0
for i, c in xDic.items():
    if c == 1:
        resX = i

for i, c in yDic.items():
    if c == 1:
        resY = i

print(resX, resY)