n, h = map(int, input().split())
throw = []
aMax = 0
for _ in range(n):
    a, b = map(int, input().split())
    throw.append(b)
    aMax = max(aMax, a)

throw.sort(reverse=True)
cnt = 0

for v in throw:
    if v <= aMax:
        break
    cnt += 1
    h -= v
    if h <= 0:
        print(cnt)
        exit()

cnt += h // aMax
if h % aMax:
    cnt += 1

print(cnt)


