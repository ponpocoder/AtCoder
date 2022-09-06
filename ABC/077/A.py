s = input()
t = input()

for i in range(3):
    if s[i] != t[2-i]:
        print("NO")
        exit()

print("YES")
