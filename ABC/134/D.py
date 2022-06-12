n = int(input())
a = list(map(int, input().split()))
b = [0] * (n+1)
cnt = 0
res = []
for i in range(n, 0, -1):
    curr = 0
    for j in range(i, n+1, i):
        curr += b[j]
    
    if curr & 1 != a[i-1]:
        b[i] = 1
        cnt += 1
        res.append(i)

print(cnt)
if cnt:
    print(*res)