n = int(input())
res = [0]

for _ in range(n-1):
    c, s, f = map(int, input().split())
    for i in range(len(res)):
        if res[i] <= s:
            res[i] = s + c
        else:
            diff = res[i] - s
            diff %= f
            if diff == 0:
                res[i] += c
            else:
                res[i] += f - diff + c
    res.append(0)

for re in res:
    print(re)