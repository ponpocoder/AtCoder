n = int(input())
p = list(map(int, input().split()))

cnt = 0

for i in range(n-1):
    if p[i] == i + 1:
        p[i], p[i+1] = p[i+1], p[i]
        cnt += 1

if n == p[n-1]:
    cnt += 1

print(cnt)