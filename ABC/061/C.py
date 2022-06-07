from collections import defaultdict

n, k = map(int, input().split())
dic = defaultdict(int)
s = set()

for _ in range(n):
    a, b = map(int, input().split())
    s.add(a)
    dic[a] += b

t = list(s)
t.sort()

cnt = 0

for i in range(len(t)):
    cnt += dic[t[i]]

    if cnt >= k:
        print(t[i])
        exit()