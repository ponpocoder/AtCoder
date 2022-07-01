s = input()
s = s.replace("BC", "D")

curr = 0
res = 0

for c in s:
    if c == "A":
        curr += 1
    elif c == "D":
        res += curr
    else:
        curr = 0

print(res)