n, k = map(int, input().split())
x, y = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

def haveSameSlope(a, b, c):
    return (x[a] - x[b]) * (y[b] - y[c]) == (x[b] - x[c]) * (y[a] - y[b])

def judge(a, b):
    curr = [a, b]
    cnt = 2

    for i in range(b+1, n):
        if haveSameSlope(a, b, i):
            cnt += 1
            curr.append(i)
    
    for i in range(cnt):
        for j in range(i+1, cnt):
            seen[curr[i]][curr[j]] = True
    
    return cnt >= k

if k == 1:
    print("Infinity")
    exit()

seen = [[False] * n for _ in range(n)]
res = 0

for i in range(n):
    for j in range(i+1, n):
        if not seen[i][j] and judge(i, j):
            res += 1

print(res)
