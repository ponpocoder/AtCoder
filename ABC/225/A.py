s = input()
chars = set()

for c in s:
    if c not in chars:
        chars.add(c)

if len(chars) == 3:
    print(6)
elif len(chars) == 2:
    print(3)
else:
    print(1)