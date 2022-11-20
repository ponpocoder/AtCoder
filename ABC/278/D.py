from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dic = defaultdict(int)
for i, v in enumerate(a):
    dic[i] = v

q = int(input())
curr = 0
for _ in range(q):
    query = list(map(int, input().split()))
    x = query[0]
    if x == 1:
        dic = defaultdict(int)
        curr = query[1]
    elif x == 2:
        i, y = query[1], query[2]
        i -= 1
        if i in dic:
            dic[i] += y
        else:
            dic[i] = curr + y
    else:
        i = query[1]
        i -= 1
        if i in dic:
            print(dic[i])
        else:
            print(curr)
    # print(*a)
