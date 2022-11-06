s = input()

for i in reversed(range(len(s))):
    if s[i] == "a":
        print(i+1)
        exit()

print(-1)
