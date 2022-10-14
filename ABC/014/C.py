n = int(input())
t = 1000002
x = [0] * t

for _ in range(n):
    a, b = map(int, input().split())
    x[a] += 1
    x[b+1] -= 1

res = 0
curr = 0
for i in range(t):
    curr += x[i]
    res = max(res, curr)

print(res)
