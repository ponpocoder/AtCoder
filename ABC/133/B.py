n, d = map(int, input().split())
x = []

for _ in range(n):
    curr = list(map(int, input().split()))
    x.append(curr)

def getDistance(a, b):
    curr = 0
    for i in range(len(a)):
        curr += (a[i] - b[i]) ** 2
    return curr ** 0.5

res = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        distance = getDistance(x[i], x[j])
        if int(distance) == distance:
            res += 1

print(res)
