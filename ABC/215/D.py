n, m = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for v in a:
    for i in range(1, v):
        if i*i > v:
            break
        if v % i == 0:
            s.add(i)
            s.add(v//i)

if 1 in s:
    s.remove(1)
    
l = list(s)
for v in l:
    for i in range(v, m+1, v):
        s.add(i)

res = []
for i in range(1, m+1):
    if i not in s:
        res.append(i)

print(len(res))
for v in res:
    print(v)