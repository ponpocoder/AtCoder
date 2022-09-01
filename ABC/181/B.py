n = int(input())

cnt = [0] * (10**6+1)

for _ in range(n):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b] -= 1

curr = 0
res = 0
for i in range(10**6+1):
    res += curr*i
    curr += cnt[i]

print(res)
