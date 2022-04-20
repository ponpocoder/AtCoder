n = int(input())
s = input()
res = 0

for i in range(len(s)):
    if i + 3 <= len(s) and s[i:i+3] == "ABC":
        res += 1

print(res)

