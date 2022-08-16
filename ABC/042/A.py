s = list(map(int, input().split()))

d, e = 0, 0

for c in s:
    if c == 5:
        d += 1
    if c == 7:
        e += 1

if d == 2 and e == 1:
    print("YES")
else:
    print("NO")
