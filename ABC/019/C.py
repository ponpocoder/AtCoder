n = int(input())
s = set()
a = list(map(int, input().split()))
cnt = 0

for i in range(n):
    while a[i] and a[i] % 2 == 0:
        a[i] //= 2
    if a[i] not in s:
        cnt += 1
    s.add(a[i])

print(cnt)
