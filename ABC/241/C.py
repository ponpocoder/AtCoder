import sys
n = int(input())
matrix = []
for _ in range(n):
    s = input()
    matrix.append(s)

    def canForm(r, c):
        return True
for i in range(n):
    for j in range(n):
        if canForm(i, j):
            print("Yes")
            sys.exit()

print("No")