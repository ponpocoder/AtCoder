n, q = map(int, input().split())

c = [0] * (n+1)

for _ in range(q):
    l, r = map(int, input().split())
    c[l-1] += 1
    c[r] += 1

res = []
curr = 0
for i in range(n):
    curr += c[i]
    curr %= 2
    res.append(str(curr))

print("".join(res))
