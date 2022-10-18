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
