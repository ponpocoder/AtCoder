n = int(input())
s = input()
res = ""
opening = 0
for c in s:
    if c == "(":
        res += "("
        opening += 1
    else:
        if opening > 0:
            res += ")"
            opening -= 1
        else:
            res = "(" + res + ")"

res += ")" * opening
print(res)