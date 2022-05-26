import sys

n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
row = (b[0][0] - 1) // 7
col = (b[0][0] - 1) % 7

if col + len(b[0]) >= 8:
    print("No")
    sys.exit()

for i in range(n):
    if i < n - 1 and b[i+1][0] != b[i][0] + 7:
        print("No")
        sys.exit()
    for j in range(m - 1):
        if b[i][j+1] != b[i][j] + 1:
            print("No")
            sys.exit()

print("Yes")