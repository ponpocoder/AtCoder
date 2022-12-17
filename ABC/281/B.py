s = input()
res = True

if len(s) != 8:
    res = False
if s[0].isdigit():
    res = False
if s[-1].isdigit():
    res = False

if res:
    if not s[1:7].isdigit() or s[1] == '0':
        res = False

if res:
    print("Yes")
else:
    print("No")
