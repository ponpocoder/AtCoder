n = int(input())
a = [list(input()) for _ in range(n)]

ok = True

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][j] == "D" and a[j][i] == "D":
            continue
        if a[i][j] == "W" and a[j][i] == "L":
            continue
        if a[i][j] == "L" and a[j][i] == "W":
            continue
        ok = False

if ok:
    print("correct")
else:
    print("incorrect")
