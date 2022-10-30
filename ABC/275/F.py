n, m = map(int, input().split())
a = list(map(int, input().split()))

s = set()
s.add(0)
res = [-1] * (m+1)


for i, v in enumerate(a):
    t = s.copy()
    for x in s:
        t.add(v+x)
        t.add(v-x)

    for j in range(1, m+1):
        if j in t and res[j] == -1:
            res[j] = i+1
    s = t

for i in range(1, m+1):
    print(res[i])
        
