n = int(input())
a = [0] + list(map(int, input().split())) + [0]
s = 0
for i in range(n+1):
    s += abs(a[i+1] - a[i])

for i in range(n):
    res = s - (abs(a[i+1] - a[i]) + abs(a[i+2] - a[i+1])) + abs(a[i+2] - a[i])
    print(res)