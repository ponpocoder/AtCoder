n, m = map(int, input().split())
cnt = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cnt[a] += 1
    cnt[b] += 1

x = 0

for v in cnt:
    if v % 2:
        print("NO")
        exit()

print("YES")
