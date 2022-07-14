n = int(input())
s = input()

w = 0
r = 0
cnt = 0
for c in s:
    if c == "W":
        w += 1
    else:
        r += 1

cnt = 0
for i in range(r):
    if s[i] == "W":
        cnt += 1

print(cnt)