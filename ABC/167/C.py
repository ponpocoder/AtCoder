n, m, x = map(int, input().split())
book = [list(map(int, input().split())) for _ in range(n)]
INF = 100100100
res = INF
for i in range(1<<n):
    curr = 0
    score = [0] * m
    for j in range(n):
        if i>>j &1:
            curr += book[j][0]
            for k in range(m):
                score[k] += book[j][k+1]

    flag = True
    for v in score:
        if v < x:
            flag = False
            break
    if flag:
        res = min(res, curr)

if res != INF:
    print(res)
else:
    print(-1)
