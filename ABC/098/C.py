n = int(input())
s = input()
r = [0] * n
l = [0] * n

curr = 0
for i in range(n):
    l[i] = curr
    if s[i] == "W":
        curr += 1
    
curr = 0
for i in reversed(range(n)):
    r[i] = curr
    if s[i] == "E":
        curr += 1
res = n

for i in range(n):
    res = min(res, l[i]+r[i])

print(res)