from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cntA = [0] * n
dic = defaultdict(lambda:1<<60)
cnt = 0

for i, x in enumerate(a):
    if x not in dic:
        cnt += 1
        dic[x] = cnt
    cntA[i] = cnt

cntB = [0] * n
maxB = [0] * n
m = 0
s = set()

for i, x in enumerate(b):
    s.add(x)
    m = max(m, dic[x])
    cntB[i] = len(s)
    maxB[i] = m

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if cntA[x] == cntB[y] == maxB[y]:
        print("Yes")
    else:
        print("No")
