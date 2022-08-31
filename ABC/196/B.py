x = input()

i = 0
res = ""
while i < len(x) and x[i] != ".":
    res += x[i]
    i += 1

print(res)
