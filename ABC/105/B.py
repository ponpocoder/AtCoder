import sys
n = int(input())
curr = 0
for i in range(n // 4 + 1):
    curr = n - 4 * i
    for j in range(curr // 7 + 1):
        if 4 * i + 7 * j == n:
            print("Yes")
            sys.exit()

print("No")