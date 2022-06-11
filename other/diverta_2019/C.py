n = int(input())
res = 0 
cntA = 0
cntB = 0
cntAB = 0
for _ in range(n):
    s = input()
    if s[0] == "B" and s[-1] == "A":
        cntAB += 1
    elif s[0] == "B":
        cntB += 1
    elif s[-1] == "A":
        cntA += 1

    for i in range(len(s) - 1):
        if s[i] == "A" and s[i+1] == "B":
            res += 1

if cntA == cntB == 0:
    cnt = max(cntAB - 1, 0)
else:
    cnt = min(cntA, cntB) + cntAB
res += cnt
print(res)