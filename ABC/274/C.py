n = int(input())
a = list(map(int, input().split()))

n2 = 2*n + 2
cnt = [0] * n2

for i, v in enumerate(a):
    c, d = 2*(i+1), 2*(i+1)+1
    print(i, v, c, d)
    cnt[c] = cnt[d] = cnt[v]+1

cnt = cnt[1:]
for v in cnt:
    print(v)
