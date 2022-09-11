s = input()
n = len(s)

cnt = [0] * 3

for c in s:
    cnt[int(c) % 3] += 1

curr = 0
for i in range(3):
    curr += i * cnt[i]

res = 100
for i in range(3):
    for j in range(3):
        if cnt[1] < i or cnt[2] < j or i + j == n:
            continue
        nx = curr
        nx -= i
        nx -= j * 2
        if nx % 3 == 0:
            res = min(res, i+j)

print(res if res != 100 else -1)
