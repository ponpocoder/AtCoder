t = int(input())


def extgcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = extgcd(b, a % b)
    return (g, y, x - (a // b) * y)


for _ in range(t):
    n, s, k = map(int, input().split())
    g, x, y = extgcd(k, n)
    if s % g != 0:
        print(-1)
    else:
        n //= g
        s //= g
        k //= g
        res = ((x * (-s)) % n + n) % n
        print(res)
