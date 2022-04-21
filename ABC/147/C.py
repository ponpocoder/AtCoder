n = int(input())
testimonies = []

for _ in range(n):
    testimony = []
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        testimony.append((x - 1, y))
    testimonies.append(testimony)

res = 0

for i in range(2**n):
    flag = 1
    honest = []
    unkind = []
    for j in range(n):
        if (i >> j) & 1 == 1:
            honest.append(j)
        else:
            unkind.append(j)
    
    for h in honest:
        for t in testimonies[h]:
            if t[1] == 1 and t[0] in unkind:
                flag = 0
                break
            elif t[1] == 0 and t[0] in honest:
                flag = 0
                break
    
    if flag == 1:
        res = max(res, len(honest))

print(res)
