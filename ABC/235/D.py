from collections import deque
a, n = map(int, input().split())

m = 1
while m <= n:
    m *= 10

score = [-1] * m
score[1] = 0
q = deque()
q.append(1)

while q:
    curr = q.popleft()
    currScore = score[curr]

    case1 = a * curr
    if case1 < m and score[case1] == -1:
        score[case1] = currScore + 1
        q.append(case1)
    
    if curr >= 10 and curr % 10 != 0:
        strCurr = str(curr)
        newCurr = int(strCurr[-1]+strCurr[:-1])
        if newCurr < m and score[newCurr] == -1:
            score[newCurr] = currScore + 1
            q.append(newCurr)

print(score[n])
