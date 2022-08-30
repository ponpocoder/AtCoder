n = int(input())
divisors = []

for i in range(2, n+1):
    if i*i > n:
        break
    cnt = 0
    while n % i == 0:
        n //= i
        cnt += 1
    divisors.append((i, cnt))

if n != 1:
    divisors.append((n, 1))
divisors.sort()

res = 0
for v, cnt in divisors:
    if v == 1:
        continue
    curr = 1
    while curr <= cnt:
        cnt -= curr
        curr += 1
        res += 1
print(res)
