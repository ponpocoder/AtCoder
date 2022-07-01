data = [0] * n

def add(p, x):
    p += 1
    while p <= n:
        data[p - 1] += x
        p += p & -p
    
def sum(i):
    t = 0
    while i > 0:
        t += data[i - 1]
        i -= i & -i
    return t
