s = input()
t = input()

if len(s) > len(t):
    print("No")
    exit()

a = []
b = []

curr = "-1"
cnt = 1
for i in range(len(s)):
    if s[i] != curr:
        if i:
            a.append((curr, cnt))
        cnt = 1
        curr = s[i]
    else:
        cnt += 1
a.append((curr, cnt))

curr = "-1"
cnt = 1
for i in range(len(t)):
    if t[i] != curr:
        if i:
            b.append((curr, cnt))
        cnt = 1
        curr = t[i]
    else:
        cnt += 1
b.append((curr, cnt))

# print(a)
# print(b)

if len(a) != len(b):
    print("No")
    exit()
else:
    for i in range(len(a)):
        ca, na = a[i]
        cb, nb = b[i]
        if ca != cb or na > nb:
            print("No")
            exit()
        elif na == 1 and na < nb:
            print("No")
            exit()

print("Yes")
