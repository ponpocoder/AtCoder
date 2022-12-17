n = int(input())
s = list(input())

found = False
for i, c in enumerate(s):
    if found:
        if c == '"':
            found = False
    else:
        if c == ',':
            s[i] = '.'
        elif c == '"':
            found = True

print("".join(s))
