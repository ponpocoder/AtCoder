s = list(input())
res = 100
t = set(s)

for c in t:
    curr = 0
    u = s.copy()

    while len(set(u)) > 1:
        u2 = []
        for i in range(len(u)-1):
            if u[i] == c or u[i+1] == c:
                u2.append(c)
            else:
                u2.append(u[i])
        u = u2
        curr += 1
    
    res = min(res, curr)

print(res)
