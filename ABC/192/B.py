s = input()

flag = True
for i in range(len(s)):
    if i % 2 == 0 and s[i].lower() != s[i]:
        flag = False
    if i % 2 and s[i].upper() != s[i]:
        flag = False

print("Yes" if flag else "No")
