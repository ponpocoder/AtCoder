k = int(input())
s = input()[:4]
t = input()[:4]

cards = [k] * 10
cntS = [1] * 10
cntT = [1] * 10

for u, v in zip(s, t):
    cards[int(u)] -= 1
    cards[int(v)] -= 1
    cntS[int(u)] += 1
    cntT[int(v)] += 1

total = (9*k-8)*(9*k-9)
def f(cnt, i):
    curr = 0
    cnt[i] += 1 
    for j in range(10):
        curr += j * 10 ** cnt[j]
    cnt[i] -= 1
    return curr

curr = 0
for i in range(1, 10):
    for j in range(1, 10):
        if f(cntS, i) > f(cntT, j):
            if i == j:
                curr += cards[i] * (cards[i] - 1)
            else:
                curr += cards[i] * cards[j]

print(curr / total)