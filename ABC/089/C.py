n = int(input())

m, a, r, c, h = 0, 0, 0, 0, 0

for _ in range(n):
    s = input()
    ch = s[0]
    if ch == "M":
        m += 1
    elif ch == "A":
        a += 1
    elif ch == "R":
        r += 1
    elif ch == "C":
        c += 1
    elif ch == "H":
        h += 1

march = [m, a, r, c, h]
res = 0
for i in range(len(march)):
    for j in range(i + 1, len(march)):
        for k in range(j + 1, len(march)):
            a, b, c = march[i], march[j], march[k]
            res += a * b * c

print(res)