n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = []
s = 0
cnt = 0
for i in range(n):
    if a[i] > b[i]:
        c.append(a[i] - b[i])
    elif a[i] < b[i]:
        s += b[i] - a[i]
        cnt += 1

p = 0
c.sort(reverse=True)

while p < len(c) and s > 0:
    s -= c[p]
    p += 1
    cnt += 1

if s <= 0:
    print(cnt)
else:
    print(-1)