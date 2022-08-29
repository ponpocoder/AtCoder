n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dic = {}

for v in a:
    dic[v-1] = dic.get(v-1, 0) + 1

res = 0

for i in range(n):
    idx = c[i] - 1
    if idx >= n:
        continue
    res += dic.get(b[idx]-1, 0)

print(res)
