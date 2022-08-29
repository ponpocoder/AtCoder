n, k = map(int, input().split())
s = []

for _ in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

s.sort()

for a, b in s:
    if a > k:
        print(k)
        exit()
    k += b

print(k)
