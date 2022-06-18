n = int(input())
s = input()

if n == 1:
    print(0)
    exit()

b = [0] * (n)
w = [0] * (n)

curr = 0
for i in range(n):
    b[i] = curr
    if s[i] == "#":
        curr += 1

curr = 0
for i in reversed(range(n)):
    w[i] = curr
    if s[i] == ".":
        curr += 1

# print(b)
# print(w)

res = n
for i in range(n):
    res = min(res, b[i]+w[i])

print(res)