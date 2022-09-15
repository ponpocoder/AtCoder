a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
bingo = [[-1] * 3 for _ in range(3)]

for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                bingo[i][j] = 0
flag = False
for i in range(3):
    cnt = 0
    for j in range(3):
        if bingo[i][j] == 0:
            cnt += 1
    if cnt == 3:
        flag = True

for i in range(3):
    cnt = 0
    for j in range(3):
        if bingo[j][i] == 0:
            cnt += 1
    if cnt == 3:
        flag = True

cnt = 0
for i in range(3):
    if bingo[i][i] == 0:
        cnt += 1
    if cnt == 3:
        flag = True

for i in range(3):
    if bingo[2-i][i] == 0:
        cnt += 1
    if cnt == 3:
        flag = True

print("Yes" if flag else "No")
