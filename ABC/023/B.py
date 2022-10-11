from collections import deque

n = int(input())
s = input()
curr = deque()
curr.append("b")
i = 1
while True:
    if len(curr) == n and "".join(curr) == s:
        print(i-1)
        exit()
    if len(curr) > n:
        print(-1)
        exit()
    if i % 3 == 0:
        curr.appendleft("b")
        curr.append("b")
    elif i % 3 == 1:
        curr.appendleft("a")
        curr.append("c")
    else:
        curr.appendleft("c")
        curr.append("a")
    i += 1
