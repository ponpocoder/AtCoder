n = int(input())
b = list(map(int, input().split()))
res = []
for i in range(n):
    for j in range(len(b) - 1, -1, -1):
        if b[j] == j+1:
            b.pop(j)
            res.append(j+1)
            break

res.reverse()
if not b:
    for v in res:
        print(v)
else:
    print(-1)