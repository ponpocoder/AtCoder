from math import ceil

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

a = [0] + a
a += [n+1]

d = []
for i in range(1, len(a)):
    diff = a[i] - a[i-1] - 1
    if diff:
        d.append(diff)

k = min(d) if d else 0
cnt = 0

for i in range(len(d)):
    cnt += ceil(d[i]/k)

print(cnt)