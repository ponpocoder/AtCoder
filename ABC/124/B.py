n = int(input())
h = list(map(int, input().split()))

ch = 0
cnt = 0
for i in range(n):
    if h[i] >= ch:
        cnt += 1
    ch = max(ch, h[i])

print(cnt)
