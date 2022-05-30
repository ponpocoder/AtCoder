s = input()
res = []
for c in s:
    if c == "0":
        res.append("0")
    elif c == "1":
        res.append("1")
    else:
        if res:
            res.pop()

print("".join(res))