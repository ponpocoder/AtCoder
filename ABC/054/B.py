n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

def isSame(r, c):
    for i in range(r, r+m):
        for j in range(c, c+m):
            if a[i][j] != b[i-r][j-c]:
                return False
    return True

for i in range(n-m+1):
    for j in range(n-m+1):
        if isSame(i, j):
            print("Yes")
            exit()

print("No")