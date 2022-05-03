s = input()
a = int(s)
b = int(s[1:] + s[0])
c = int(s[2:] + s[:2])

print(a+b+c)