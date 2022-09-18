x = int(input())
s = []

k = 0
while x:
    if x % 2:
        s.append(k)
    x >>= 1
    k += 1

res = [0]
for v in s:
    for i in range(len(res)):
        res.append(res[i]+2**v)

for v in res:
    print(v)
