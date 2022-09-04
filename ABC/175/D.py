n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

for i in range(n):
    p[i] -= 1

res = float("-inf")
for i in range(n):
    curr = i
    score = []
    total = 0
    while True:
        curr = p[curr]
        score.append(c[curr])
        total += c[curr]
        if curr == i:
            break
    l = len(score)
    cs = 0
    for j in range(l):
        if j > k:
            break
        cs += score[j]
        curr = cs
        if total > 0:
            curr += total * (k-(j+1)) // l
        res = max(res, curr)

print(res)
