n = int(input())
s = input()
t = input()

mod = 10**9 + 7

curr = 3
res = 1

i = 0
flag = False  # 1つ前の列の色が同じ
while i < n:
    if s[i] == t[i]:
        if not flag:
            if i == 0:
                res *= 3
            else:
                res *= 1
        else:
            res *= curr
        curr = 2
        flag = True
        i += 1
    else:
        if not flag:
            if i == 0:
                res *= 6
            else:
                res *= 3
            curr = 1
        else:
            res *= 2
            curr = 2
        flag = False
        i += 2
    res %= mod

print(res)
