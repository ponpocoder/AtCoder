from collections import defaultdict

s = input()
t = input()

st = defaultdict(str)
ts = defaultdict(str)

for a, b in zip(s, t):
    if a not in st:
        st[a] = b
    elif st[a] != b:
        print("No")
        exit()

for a, b in zip(s, t):
    if b not in ts:
        ts[b] = a
    elif ts[b] != a:
        print("No")
        exit()
    
print("Yes")