n, s, d = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    if x >= s or y <= d:
        continue
    print("Yes")
    exit()

print("No")
