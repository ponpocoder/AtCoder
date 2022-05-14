w = int(input())

res = []

for i in range(1, 100):
    res.append(i)
for i in range(100, 10000, 100):
    res.append(i)
for i in range(10000, 1000000, 10000):
    res.append(i)

print(len(res))
print(*res)