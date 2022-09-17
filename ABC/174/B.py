n, d = map(int, input().split())
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())
    curr = x**2 + y**2
    if curr <= d**2:
        cnt += 1

print(cnt)
