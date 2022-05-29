from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

dic = defaultdict(int)

for v in a:
    dic[v] += 1

cnt = []
for c in dic.values():
    cnt.append(c)

cnt.sort()

res = 0
curr = len(cnt)
if curr <= k:
    print(res)
else:
    diff = curr - k
    for i in range(diff):
        res += cnt[i]
    print(res)

