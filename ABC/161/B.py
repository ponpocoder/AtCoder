n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
x = s / (4*m)

cnt = 0
for v in a:
    if v >= x:
        cnt += 1

print("Yes" if cnt >= m else "No")
