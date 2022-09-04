n = int(input())
x = 55555
primes = [True] * (x+1)
primes[0] = primes[1] = False
curr = []
for i in range(2, x+1):
    if not primes[i]:
        continue
    if i % 5 == 1:
        curr.append(i)
    for j in range(i*i, x+1, i):
        primes[j] = False

print(*curr[:n])
