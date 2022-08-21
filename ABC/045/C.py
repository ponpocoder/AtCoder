s = input()

res = 0
n = len(s) - 1

for i in range(1 << n):
    curr = 0
    for j in range(len(s)):
        if (i & 1 << j):
            res += curr * 10 + int(s[j])
            curr = 0
        else:
            curr = curr * 10 + int(s[j])
    res += curr

print(res)
