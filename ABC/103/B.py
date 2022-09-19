s = input()
t = input()
n = len(s)
for i in range(n):
    if s == t:
        print("Yes")
        exit()
    s = s[1:] + s[0]

print("No")
