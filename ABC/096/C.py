h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

def isConnected(i, j):
    flag = False
    if i > 0 and s[i-1][j] == "#":
        flag = True
    if i < h-1 and s[i+1][j] == "#":
        flag = True
    if j > 0 and s[i][j-1] == "#":
        flag = True
    if j < w-1 and s[i][j+1] == "#":
        flag = True
    return flag

for i in range(h):
    for j in range(w):
        if s[i][j] == "#" and not isConnected(i, j):
            print("No")
            exit()

print("Yes")