n, a, b, c, d = map(int, input().split())
a -= 1
b -= 1
c -= 1
d -= 1

s = input()
res = True
if c < d:
    for i in range(a+1, c):
        if s[i] == s[i-1] == "#":
            res = False
    for i in range(b+1, d):
        if s[i] == s[i-1] == "#":
            res = False
else:
    res = False
    for i in range(b, d+1):
        if s[i+1] == s[i] == s[i-1] == ".":
            res = True
            break

if res:
    print("Yes")
else:
    print("No")