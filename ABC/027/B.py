n = int(input())
a = list(map(int, input().split()))
s = sum(a)
x = s // n
if s % n != 0:
    print(-1)
    exit()

curr = 0
cnt = 0
j = 1
for i in range(n-1):
    curr += a[i]
    if curr % j == 0 and curr // j == x:
        curr = 0
        continue
    cnt += 1
    j += 1

print(cnt)
