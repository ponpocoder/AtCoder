import sys
s = input()

for i in range(len(s) - 1):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print("No")
            sys.exit()

flag = False
flag2 = False
for c in s:
    if c >= "a" and c <= "z":
        flag = True
    if c >= "A" and c <= "Z":
        flag2 = True

if flag and flag2:
    print("Yes")
else:
    print("No")