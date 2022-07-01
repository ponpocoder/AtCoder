n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = 0
curr = 0

for i in range(n):
    if a[i] > 2 * curr:
        cnt = 1
    else:
        cnt += 1
    curr += a[i]

print(cnt)