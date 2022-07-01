n = int(input())
cords = []
dic = {}
for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x, y))
cnt = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dx = cords[i][0] - cords[j][0]
        dy = cords[i][1] - cords[j][1]
        dic[(dx, dy)] = dic.get((dx, dy), 0) + 1
        cnt = max(cnt, dic[(dx, dy)])

if n == 1:
    print(1)
else:
    print(n-cnt)