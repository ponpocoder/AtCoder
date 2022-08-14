s = list(input())
cnt = 0


def swap(l, r):
    # print(l, r)
    # print(s)
    if l < r:
        for i in range(l, r):
            s[i], s[i+1] = s[i+1], s[i]
    else:
        for i in range(l, r, -1):
            s[i], s[i-1] = s[i-1], s[i]
    global cnt
    # print(s)
    cnt += abs(l-r)


for i, c in enumerate("atcoder"):
    idx = s.index(c)
    swap(idx, i)

print(cnt)
