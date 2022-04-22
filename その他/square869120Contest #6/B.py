n = int(input())
a, b = [], []

for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

time = float("inf")
# solution1
# for s in range(1, 101):
#     for g in range(1, 101):
#         curr = 0
#         for x, y in zip(a, b):
#             curr += abs(s - x) + abs(x - y) + abs(y - g)
#         res = min(curr, res)

def getTime(starts, goals):
    res = float("inf")
    for s in starts:
        for g in goals:
            curr = 0
            for x, y in zip(a, b):
                curr += abs(s - x) + abs(x - y) + abs(y - g)
            res = min(curr, res)
    
    return res

time = min(time, getTime(a, a), getTime(a, b), getTime(b, a), getTime(b, b))
print(time)