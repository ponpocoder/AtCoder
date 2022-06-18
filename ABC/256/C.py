h1, h2, h3, w1, w2, w3 = map(int, input().split())
r1 = set()
r2 = set()
r3 = set()

for i in range(1,h1):
    for j in range(1,h1):
        for k in range(1,h1):
            if i + j + k == h1:
                r1.add((i, j, k))
for i in range(1,h2):
    for j in range(1,h2):
        for k in range(1,h2):
            if i + j + k == h2:
                r2.add((i, j, k))
for i in range(1,h3):
    for j in range(1,h3):
        for k in range(1,h3):
            if i + j + k == h3:
                r3.add((i, j, k))

cnt = 0
curr = []
for x1 in r1:
    curr.append(x1)
    for x2 in r2:
        curr.append(x2)
        for x3 in r3:
            curr.append(x3)
            if curr[0][0] + curr[1][0] + curr[2][0] == w1 and curr[0][1] + curr[1][1] + curr[2][1] == w2 and curr[0][2] + curr[1][2] + curr[2][2] == w3:
                cnt += 1
            curr.pop()
        curr.pop()
    curr.pop()

print(cnt)