from collections import deque
n = int(input())
s = input()


q = deque([n])
for i in reversed(range(n)):
    if s[i] == "L":
        q.append(i)
    else:
        q.appendleft(i)

print(*list(q))