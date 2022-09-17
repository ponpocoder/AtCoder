n = int(input())
p = list(map(int, input().split()))
cnt = [0] * n
for i, v in enumerate(p):
    if v >= i:
        cnt[v-i] += 1
    else:
        cnt[n-(i-v)] += 1

res = 0
# print(cnt)
for i in range(n):
    res = max(res, cnt[i-1]+cnt[i]+cnt[(i+1) % n])
print(res)
