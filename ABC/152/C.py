n = int(input())
p = list(map(int, input().split()))

curr = p[0]
cnt = 0
for i in range(n):
    if p[i] <= curr:
        cnt += 1
    curr = min(curr, p[i])

print(cnt)
