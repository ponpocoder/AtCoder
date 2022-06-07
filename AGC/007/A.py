h, w = map(int, input().split())
a = [input() for _ in range(h)]
cnt = 0

for r in range(h):
    for c in range(w):
        if a[r][c] == "#":
            cnt += 1

if cnt == h + w - 1:
    print("Possible")
else:
    print("Impossible")