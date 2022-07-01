s = input()
k = int(input())

t = list(s)
cnt = 0
for i in range(1, len(t)):
    if t[i] == t[i-1]:
        t[i] = "0"
        cnt += 1

u = list(s+s)
cnt2 = 0
for i in range(1, len(u)):
    if u[i] == u[i-1]:
        u[i] = "0"
        cnt2 += 1

c = s[0]
allSame = True
for i in range(1, len(s)):
    if s[i] != c:
        allSame = False

if allSame:
    res = (k//2*cnt2)
    if k % 2:
        res += cnt
    print(res)
else:
    res = (k-1)*(cnt2-cnt)+cnt
    print(res)