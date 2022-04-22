import sys
n, m = map(int, input().split())

conds = []
for _ in range(m):
    s, c = map(int, input().split())
    conds.append((s, c))

for i in range(1000):
    strN = str(i)
    if len(strN) < n:
        continue
    flag = True
    for s, c in conds:
        if strN[s - 1] != str(c):
            flag = False
            break

    if flag:
        print(i)
        sys.exit()

print(-1)