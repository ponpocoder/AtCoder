from collections import defaultdict

s = input()
d = defaultdict(int)

for c in s:
    d[int(c)] += 1

def solve():
    if len(s) == 1:
        if int(s[0]) == 8:
            return True
        else:
            return False
    elif len(s) == 2:
        if (int(s[0]) * 10 + int(s[1])) % 8 == 0 or (int(s[1]) * 10 + int(s[0])) % 8 == 0:
            return True
        else:
            return False
    for i in range(1, 10):
        if not d[i]:
            continue
        d[i] -= 1
        for j in range(1, 10):
            if not d[j]:
                continue
            d[j] -= 1
            for k in range(1, 10):
                if not d[k]:
                    continue
                curr = 100*i + 10*j + k 
                if curr % 8 == 0:
                    return True
            d[j] += 1
        d[i] += 1

    return False

if solve():
    print("Yes")
else:
    print("No")