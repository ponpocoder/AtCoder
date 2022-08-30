s = input()

flag = True

if s[0] != "A":
    flag = False

cnt = 0
for c in s[2:len(s)-1]:
    if c == "C":
        cnt += 1

if cnt != 1:
    flag = False

for i in range(1, len(s)):
    if s[i] == "C":
        continue
    if s[i].lower() != s[i]:
        flag = False

if flag:
    print("AC")
else:
    print("WA")
