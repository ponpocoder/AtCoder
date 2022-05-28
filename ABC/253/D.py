import math
n, a, b = map(int, input().split())

total = n * (n + 1) // 2
nA = n // a
dA = a * nA
sumA = nA*(a+dA)//2
nB = n // b
dB = b * nB
sumB = nB*(b+dB)//2
c = a * b // math.gcd(a, b)
nC = n // c
dC = c * nC
sumC = nC*(c+dC)//2

res = total - sumA - sumB + sumC
print(res)

