n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

res = a[0]

for i in range(n):
    res = gcd(res, a[i])

print(res)