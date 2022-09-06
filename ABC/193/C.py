n = int(input())

res = 0
s = set()
for i in range(2, n):
    if i * i > n:
        break
    curr = i * i
    while curr <= n and curr not in s:
        res += 1
        s.add(curr)
        curr *= i

print(n-res)
