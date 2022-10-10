a, b = input().split()

x = ""
for _ in range(int(a)):
    x += b
y = ""
for _ in range(int(b)):
    y += a

if x < y:
    print(x)
else:
    print(y)
