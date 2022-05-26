import sqlite3


n = int(input())
s = input()
q = int(input())

s1 = list(s[:n])
s2 = list(s[n:])

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        a -= 1
        b -= 1
        if a < n and b < n:
            s1[a], s1[b] = s1[b], s1[a]
        elif a < n and b >=n:
            s1[a], s2[b-n] = s2[b-n], s1[a]
        else:
            s2[a-n], s2[b-n] = s2[b-n], s2[a-n]
    else:
        s1, s2 = s2, s1

s = "".join(s1) + "".join(s2)
print(s)