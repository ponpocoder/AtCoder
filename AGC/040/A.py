s = input()
n = len(s) + 1

a = [0] * n

for i in range(len(s)):
    if s[i] == "<":
        a[i+1] = a[i] + 1

for i in reversed(range(len(s))):
    if s[i] == ">":
        a[i] = max(a[i+1]+1, a[i])

print(sum(a))