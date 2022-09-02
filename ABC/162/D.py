n = int(input())
s = input()


r = [0] * n
g = [0] * n
b = [0] * n

for i in range(n-2, -1, -1):
    r[i] = r[i+1]
    g[i] = g[i+1]
    b[i] = b[i+1]
    if s[i+1] == "R":
        r[i] += 1
    if s[i+1] == "G":
        g[i] += 1
    if s[i+1] == "B":
        b[i] += 1

res = 0
for i in range(n):
    for j in range(i+1, n):
        if s[i] == s[j]:
            continue
        if "R" != s[i] and "R" != s[j]:
            res += r[j]
            if 2*j-i < n and s[2*j-i] == "R":
                res -= 1
        elif "G" != s[i] and "G" != s[j]:
            res += g[j]
            if 2*j-i < n and s[2*j-i] == "G":
                res -= 1
        else:
            res += b[j]
            if 2*j-i < n and s[2*j-i] == "B":
                res -= 1

print(res)
