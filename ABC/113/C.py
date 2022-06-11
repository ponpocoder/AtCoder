n, m = map(int, input().split())

city = []

for i in range(m):
    p, y = map(int, input().split())
    city.append((p, y, i))

city.sort(key=lambda x: x[1])
pointer = [1] * (n + 1)
res = []

def getNumber(p, order):
    return "0" * (6 - len(str(p))) + str(p) + "0" * (6 - len(str(order))) + str(order)

for p, y, i in city:
    order = pointer[p]
    number = getNumber(p, order)
    res.append((i, number))
    pointer[p] += 1

res.sort()
for r in res:
    print(r[1])