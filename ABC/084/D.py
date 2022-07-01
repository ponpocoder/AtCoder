n = 10**5+1

primes = [False] * (n)

for i in range(2, n):
    isPrime = True
    for j in range(2, i):
        if j*j > i:
            break
        if i % j == 0:
            isPrime = False
            break
    
    if isPrime:
        primes[i] = True

s = [0] * (n+1)
curr = 0
for i in range(n):
    if primes[i] and primes[(i+1)//2]:
        curr += 1
    s[i] = curr

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(s[r] - s[l-1])
