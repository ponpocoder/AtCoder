n = int(input())
a = list(map(int, input().split()))
A = max(a)  + 1

cnt = [0] * A

for v in a:
    for i in range(v, A, v):
        cnt[i] += 1

res = 0
for v in a:
    if cnt[v] == 1:
        res += 1

print(res)