t = ".........."
s = [input() for _ in range(10)]

a, b, c, d = 0, 0, 0, 0
for i in range(10):
    if s[i] != t:
        a = i+1
        for j in range(10):
            if s[i][j] == "#":
                c = j + 1
                break
        for j in range(9, -1, -1):
            if s[i][j] == "#":
                d = j + 1
                break
        break

for i in range(9, -1, -1):
    if s[i] != t:
        b = i + 1
        break

print(a, b)
print(c, d)
