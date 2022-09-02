k = int(input())


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


res = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        curr = gcd(i, j)
        for h in range(1, k+1):
            res += gcd(curr, h)

print(res)
