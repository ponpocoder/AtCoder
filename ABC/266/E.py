n = int(input())

res = 0

for _ in range(n):
    curr = 0
    for j in range(1, 7):
        curr += max(j, res)
    res = curr / 6

print(res)
