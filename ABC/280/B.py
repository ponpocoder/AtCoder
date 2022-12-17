n = int(input())
s = list(map(int, input().split()))
a = []

curr = 0
for i in range(n):
    x = s[i] - curr
    a.append(x)
    curr += a[-1]

print(*a)
