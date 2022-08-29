from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] %= 200

dic = defaultdict(int)

res = 0
for v in a:
    x = (v-200) % 200
    res += dic[x]
    dic[v] += 1

print(res)
