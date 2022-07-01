h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
res = [[0] * w for _ in range(h)]
curr = []
for i, v in enumerate(a):
    for _ in range(v):
        curr.append(i+1)

for i in range(h):
    for j in range(w):
        k = j if i % 2 == 0 else w - j - 1        
        res[i][k] = curr[i*w+j]

for r in res:
    print(*r)