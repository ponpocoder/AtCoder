n = int(input())
k = int(n ** (1/3))

primes = []
isPrime = [True] * (k + 1)
isPrime[0], isPrime[1] = False, False

for i in range(2, k+1):
    if isPrime[i]:
        primes.append(i)
        for j in range(i*i, k+1, i):
            isPrime[j] = False

res = 0
l, r = 0, len(primes) - 1
while l <= r:
    if primes[l] * primes[r] ** 3 <= n:
        res += r - l
        l += 1
    else:
        r -= 1
        
print(res)