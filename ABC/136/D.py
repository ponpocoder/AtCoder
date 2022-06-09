s = input()

n = len(s)
l = [0] * n
r = [0] * n
t = [0] * n
curr = 0
for i in range(n):
    if s[i] == "R":
        curr += 1
    else:
        if curr != 0:
            l[i] =   curr // 2
            if i > 0:
                l[i-1] = curr // 2 + curr % 2
        curr = 0
curr = 0
for i in reversed(range(n)):
    if s[i] == "L":
        curr += 1
    else:
        if curr != 0:
            r[i] = curr // 2
            if i < n - 1:
                r[i+1] = curr // 2 + curr % 2
        curr = 0

for i in range(n):
    t[i] = l[i] + r[i]

print(*t)