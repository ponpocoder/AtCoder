n, m = map(int, input().split())
x = list(map(int, input().split()))

x.sort()

s = []

for i in range(1, m):
    s.append(x[i] - x[i-1])

s.sort(reverse=True)

res = 0
for i in range(n-1, len(s)):
    res += s[i]

print(res)