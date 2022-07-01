# AtCoder Library Practice Contest B "Fenwick Tree"
n, q = map(int, input().split())
a = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)

    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.bit[i] += x
            i += i & -i
    
    def sum(self, l, r):
        return self._sum(r) - self._sum(l)
    
    def _sum(self, i):
        t = 0
        while i > 0:
            t += self.bit[i]
            i -= i & -i
        return t

bit = BIT(n)

for i in range(n):
    bit.add(i, a[i])

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        p, x = query[1], query[2]
        bit.add(p, x)
    else:
        l, r = query[1], query[2]
        print(bit.sum(l, r))