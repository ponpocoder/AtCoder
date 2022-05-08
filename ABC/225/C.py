import sys

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i < n - 1 and b[i+1][0] != b[i][0] + 7:
        print("No")
        sys.exit()
    for j in range(m - 1):
        if b[i][j+1] != b[i][j] + 1:
            print("No")
            sys.exit()

print("Yes")