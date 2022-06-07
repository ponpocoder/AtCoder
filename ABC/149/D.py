n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
hands = []
res = []

for i, c in enumerate(t):
    if i < k:
        if c == "r":
            hands.append("p")
            res.append(p)
        elif c == "s":
            hands.append("r")
            res.append(r)
        else:
            hands.append("s")
            res.append(s)
    else:
        if c == "r":
            if hands[i-k] == "p" and res[i-k] != 0:
                hands.append("r")
                res.append(0)
            else:
                hands.append("p")
                res.append(p)
            
        elif c == "s":
            if hands[i-k] == "r" and res[i-k] != 0:
                hands.append("s")
                res.append(0)
            else:
                hands.append("r")
                res.append(r)
        else:
            if hands[i-k] == "s" and res[i-k] != 0:
                hands.append("p")
                res.append(0)
            else:
                hands.append("s")
                res.append(s)

print(sum(res))