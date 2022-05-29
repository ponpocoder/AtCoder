from collections import deque

n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

currT = 0
currX = 0
currY = 0

for i in range(n):
    nextT, x, y = t[i]
    d = abs(currX-x) + abs(currY-y)
    limit = nextT - currT

    if d > limit or (limit - d) % 2 == 1:
        print("No")
        exit()

    currT = nextT
    currX = x
    currY = y

print("Yes")
    
