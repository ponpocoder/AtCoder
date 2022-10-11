s = input()
curr = "-1"
cnt = 0
res = ""

for i, c in enumerate(s):
    if c == curr:
        cnt += 1
    else:
        if curr != "-1":
            res += curr + str(cnt)
        curr = c
        cnt = 1
res += curr + str(cnt)
print(res)
