n = int(input())
s = input()


def check(x):
    for i in range(1, n+1):
        c = s[i % n]
        if x[i % n] == 0:
            if c == "o":
                if x[(i+1) % n] == None:
                    x[(i+1) % n] = x[i-1]
                else:
                    if x[(i+1) % n] != x[i-1]:
                        return []
            else:
                if x[(i+1) % n] == None:
                    x[(i+1) % n] = x[i-1] ^ 1
                else:
                    if x[(i+1) % n] == x[i-1]:
                        return []
        else:
            if c == "o":
                if x[(i+1) % n] == None:
                    x[(i+1) % n] = x[i-1] ^ 1
                else:
                    if x[(i+1) % n] == x[i-1]:
                        return []
            else:
                if x[(i+1) % n] == None:
                    x[(i+1) % n] = x[i-1]
                else:
                    if x[(i+1) % n] != x[i-1]:
                        return []
    return x


a = [0, 0, 1, 1]
b = [0, 1, 0, 1]

for i in range(4):
    x = [a[i]] + [b[i]] + [None] * (n-2)
    curr = check(x.copy())
    if curr != []:
        for j in range(n):
            if curr[j] == 0:
                curr[j] = "S"
            else:
                curr[j] = "W"
        print("".join(curr))
        exit()

print(-1)
