s = input()

cnt = 0
res = 0
for c in s:
    if c == "R":
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)

print(res)
