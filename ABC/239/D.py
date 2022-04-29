import sys
a, b, c, d = map(int, input().split())

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(a, b + 1):
    hasPrime = False
    for j in range(c, d + 1):
        if isPrime(i+j):
            hasPrime = True
    if not hasPrime:
        print("Takahashi")
        sys.exit()

print("Aoki")
