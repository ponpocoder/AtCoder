from collections import defaultdict

class sieve:
    def __init__(self, n):
        self.n = n + 1
        self.primes = [None] * self.n
        self.primes[0] = self.primes[1] = 1
        self.sieve()

    def sieve(self):
        for i in range(2, self.n):
            if self.primes[i]:
                continue
            self.primes[i] = i
            for j in range(i*i, self.n, i):
                if self.primes[j]:
                    continue
                self.primes[j] = i

    def factorList(self, x):
        res = []
        while x != 1:
            res.append(self.primes[x])
            x //= self.primes[x]
        return res

    def factor(self, x):
        fl = self.factorList(x)
        dic = defaultdict(int)
        for v in fl:
            dic[v] += 1
        return dic

def powmod(a, b, mod):
    if b == 0:
        return 1
    curr = powmod(a, b//2, mod)
    curr *= 2
    if b % 2:
        curr *= a
    return curr % mod

n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

sieve = sieve(1000001)
mp = defaultdict(int)
for i in range(n):
    dic = sieve.factor(a[i])
    for key, value in dic.items():
        mp[key] = max(mp[key], value)

lcm = 1
for key, value in mp.items():
    for _ in range(value):
        lcm *= key
        lcm %= mod

res = 0
for i in range(n):
    res += lcm * pow(a[i], mod-2, mod)
    res %= mod

print(res)
