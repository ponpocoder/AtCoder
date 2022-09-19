s = input()
n = len(s)

for i in range(n):
    if i < n - 1:
        if s[i] == s[i+1]:
            print(i+1, i+2)
            exit()
    if i < n - 2:
        if s[i] == s[i+2]:
            print(i+1, i+3)
            exit()

print(-1, -1)
