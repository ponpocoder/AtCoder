n = int(input())
s = input()

res = 0

for i in range(n):
    curr = len(set(s[:i]) & set(s[i:]))
    res = max(res, curr)

print(res)
