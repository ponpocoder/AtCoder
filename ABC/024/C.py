n, d, k = map(int, input().split())
lr = []

for _ in range(d):
    x, y = map(int, input().split())
    lr.append((x, y))


def find(left, right):
    curr = left
    for i in range(d):
        l, r = lr[i]
        if l <= curr:
            curr = max(curr, r)
        if curr >= right:
            return i+1

    return -1


def find2(left, right):
    curr = right
    for i in range(d):
        l, r = lr[i]
        if r >= curr:
            curr = min(curr, l)
        if curr <= left:
            return i+1

    return -1


for _ in range(k):
    s, t = map(int, input().split())
    if s <= t:
        print(find(s, t))
    else:
        print(find2(t, s))
