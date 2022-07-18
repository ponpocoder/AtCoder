n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = []
for i in range(n):
    score.append((a[i], n-i, b[i], a[i]+b[i]))

score.sort(reverse=True)
res = []
for i in range(x):
    res.append(n-score[i][1]+1)

score = score[x:]
score2 = []
for i in range(len(score)):
    score2.append((score[i][2], score[i][1], score[i][3]))

score2.sort(reverse=True)
for i in range(y):
    res.append(n-score2[i][1]+1)

score2 = score2[y:]
score3 = []
for i in range(len(score2)):
    score3.append((score2[i][2], score2[i][1]))

score3.sort(reverse=True)
for i in range(z):
    res.append(n-score3[i][1]+1)

res.sort()
for re in res:
    print(re)