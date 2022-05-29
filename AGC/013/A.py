n = int(input())
a = list(map(int, input().split()))

cnt = 1
i = 1

while i < n:
    while i < n and a[i] == a[i-1]:
        i += 1
    dire = a[i] - a[i-1]
    while i < n and (a[i] - a[i-1]) * dire >= 0:
        i += 1
    if i == n:
        break
    cnt += 1
    i += 1

print(cnt)