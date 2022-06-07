s = input()

res = 0
for i in range(len(s)-2, -1, -1):
    if s[i] != s[i+1]:
        res += 1

print(res)