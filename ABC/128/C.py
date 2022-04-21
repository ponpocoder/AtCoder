n, m = map(int, input().split())
lights = []
for _ in range(m):
    array = list(map(int, input().split()))
    lights.append(array[1:])

p = list(map(int, input().split()))
res = 0

for i in range(2 ** n):
    check = [False] * m
    for j, light in enumerate(lights):
        count = 0
        for l in light:
            if i >> (l - 1) & 1 == 1:
                count += 1
        if count % 2 == p[j]:
            check[j] = True

    if all(check):
        res += 1

print(res)
