s = input()
x = list(s.split("+"))
cnt = 0

for curr in x:
    flag = True
    for c in curr:
        if c == "0":
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)
