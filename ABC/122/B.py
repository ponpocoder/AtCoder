s = input()
res = 0
for i in range(len(s)):
    if s[i] != "A" and s[i] != "G" and s[i] != "C" and s[i] != "T":
        continue
    for j in range(i, len(s)):
        if s[j] != "A" and s[j] != "G" and s[j] != "C" and s[j] != "T":
            break
        res = max(res, j - i + 1)

print(res)
        