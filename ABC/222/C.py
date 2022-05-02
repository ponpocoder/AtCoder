n, m = map(int, input().split())
hands = [input() for _ in range(2*n)]

ranks = [[0, i] for i in range(2*n)]

def judge(one, two):
    if (one == "G" and two == "C") or (one == "C" and two == "P") or (one == "P" and two == "G"):
        return 1
    elif (two == "G" and one == "C") or (two == "C" and one == "P") or (two == "P" and one == "G"):
        return -1
    else:
        return 0

for i in range(m):
    for j in range(n):
        first = ranks[2*j][1]
        second = ranks[2*j+1][1]
        res = judge(hands[first][i], hands[second][i])
        if res == 1:
            ranks[2*j][0] -= 1
        elif res == -1:
            ranks[2*j+1][0] -= 1

    ranks.sort()

for w, i in ranks:
    print(i+1)