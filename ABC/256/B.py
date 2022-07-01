n = int(input())
a = list(map(int, input().split()))

cnt = 0
p = [0, 0, 0, 0]

for v in a:
    p[0] += 1
    for i in range(3, -1, -1):
        if i + v >= 4:
            cnt += p[i]
            p[i] = 0
        else:
            p[i+v] += p[i]
            p[i] = 0

print(cnt)