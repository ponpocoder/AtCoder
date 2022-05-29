n = int(input())
a = list(map(int, input().split()))

s = set()
m = 0

for v in a:
    if v < 400:
        s.add(1)
    elif v < 800:
        s.add(2)
    elif v < 1200:
        s.add(3)
    elif v < 1600:
        s.add(4)
    elif v < 2000:
        s.add(5)
    elif v < 2400:
        s.add(6)
    elif v < 2800:
        s.add(7)
    elif v < 3200:
        s.add(8)
    else:
        m += 1

if len(s) == 0:
    print(1, m)
else:
    print(len(s), len(s)+m)