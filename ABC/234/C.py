k = int(input())

n = []
curr = 1

while curr <= k:
    n.append(curr)
    curr *= 2
res = 0
for i in reversed(range(len(n))):
    if k >= n[i]:
        k -= n[i]
        res += 2 * 10 ** i

print(res)