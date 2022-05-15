s = input()

res = 0
for i in range(10000):
    curr = str(i).zfill(4)
    cnt = [0] * 10

    for c in curr:
        cnt[int(c)] = 1

    flag = True
    for i, c in enumerate(s):
        if c == "o" and cnt[i] != 1:
            flag = False
        if c == "x" and cnt[i] == 1:
            flag = False
    if flag:
        res += 1

print(res)