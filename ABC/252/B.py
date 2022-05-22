n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
curr = 0
res = []
for i, v in enumerate(a):
    if v > curr:
        curr = v
        res = [i]
    elif v == curr:
        res.append(i)

for v in b:
    for r in res:
        if r == v - 1:
            print("Yes")
            exit()

print("No")