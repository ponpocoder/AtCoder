n, p = map(int, input().split())
primes = set()

for i in range(2, p+1):
    if i*i > p:
        break
    cnt = 0
    while p % i == 0:
        p //= i
        cnt += 1
    if cnt:
        primes.add((i, cnt))

if len(primes) == 0:
    primes.add((p, 1))

primes.add((p, 1))


res = 1
for p, c in primes:
    if c >= n:
        res *= p ** (c // n)

print(res)