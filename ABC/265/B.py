n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = [0] * n

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    bonus[x] += y


for i in range(n-1):
    t += bonus[i]
    t -= a[i]

    if t <= 0:
        print("No")
        exit()

print("Yes")
