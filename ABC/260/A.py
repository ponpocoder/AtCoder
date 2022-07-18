s = input()

a = s[0]
b = s[1]
c = s[2]

if a == b == c:
    print(-1)
elif a == b:
    print(c)
elif b == c:
    print(a)
elif a == c:
    print(b)
else:
    print(a)