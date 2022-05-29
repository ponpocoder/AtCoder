s = input()
t = "keyence"
i = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[:i] + s[j:] == t:
            print("YES")
            exit()

print("NO")
