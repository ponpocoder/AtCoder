n = int(input())
aoki = 0
ab = []

for _ in range(n):
    a, b = map(int, input().split())
    aoki += a
    ab.append((2*a+b, a, b))

ab.sort(reverse=True)
takahashi = 0
cnt = 0
i = 0

while aoki >= takahashi:
    cnt += 1
    s, a, b = ab[i]
    aoki -= a
    takahashi += a + b
    i += 1

print(cnt)