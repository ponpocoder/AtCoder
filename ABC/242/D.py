import sys
s = list(input().split())
t = list(input().split())

r, g, b = 0, 0, 0
R, G, B = 0, 0, 0

for c in s:
    if c == "R":
        r += 1
    elif c == "G":
        g += 1
    else:
        b += 1

for c in t:
    if c == "R":
        R += 1
    elif c == "G":
        G += 1
    else:
        B += 1

if r == R and g == G and b == B:
    if r == g == b == 1:
        if s == t or (s[0] == t[1] and s[1] == t[2] and s[2] == t[0]) or (s[0] == t[2] and s[1] == t[0] and s[2] == t[1]):
            print("Yes")
        else:      
            print("No")
    else:
        print("Yes")
else:
    print("No")
