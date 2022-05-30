s = input()

res = 0

for i in range(len(s)):
    if s[i] == "U":
        res += 2 * i + len(s) - i - 1
    else:
        res += i + 2 * (len(s) - i - 1)

print(res)