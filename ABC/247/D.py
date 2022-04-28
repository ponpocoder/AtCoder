from collections import deque
queue = deque()

n = int(input())

for _ in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
            queue.append((q[1], q[2]))
    else:
        res = 0
        c = q[1]
        while c > 0:
            currV, currC = queue.popleft()
            if c > currC:
                c -= currC
                res += currC * currV
            else:
                res += c * currV
                print(res)
                currC -= c
                c = 0
                queue.appendleft((currV, currC))