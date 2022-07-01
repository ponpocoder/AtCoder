n, k = map(int, input().split())
s = input()
x = []

curr = "1"
l = 0

for c in s:
    if c == curr:
        l += 1
    else:
        x.append(l)
        l = 1
        curr = c
if l:
    x.append(l)
if curr == "0":
    x.append(0)

res = 0
l, r = 0, 0
curr = 0

for i in range(0, len(x), 2):
    nl = i
    nr = min(i+2*k+1, len(x))
    
    while nl > l:
        curr -= x[l]
        l += 1
    
    while r < nr:
        curr += x[r]
        r += 1
    
    res = max(res, curr)

print(res)

