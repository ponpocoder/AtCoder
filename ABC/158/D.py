from collections import deque
s = list(input())
q = int(input())

deq = deque(s)

rev = False

for _ in range(q):
    query = input().split()
    if len(query) == 1:
        rev ^= 1
    else:
        f,c = int(query[1]), query[2]
        if f == 1:
            if not rev:
                deq.appendleft(c)
            else:
                deq.append(c)
        else:
            if not rev:
                deq.append(c)
            else:
                deq.appendleft(c)


if rev:
    deq.reverse()

res = "".join(deq)
print(res)

