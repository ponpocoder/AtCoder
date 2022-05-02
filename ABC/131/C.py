import math
a, b, c, d = map(int, input().split())
a-= 1
quotientAC = a // c
quotientBC = b // c
quotientAD = a // d
quotientBD = b // d
lcm = c * d // math.gcd(c, d)
quotientAG = a // lcm
quotientBG = b // lcm

sumB = b - quotientBC - quotientBD + quotientBG
sumA = a - quotientAC - quotientAD + quotientAG

print(sumB - sumA)