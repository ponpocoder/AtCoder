n = int(input())

s = set()
t = set()

for _ in range(n):
    c = input()
    if c[0] == "!":
        c = c[1:]
        if c in s:
            print(c)
            exit()
        t.add(c)
    else:
        if c in t:
            print(c)
            exit()
        s.add(c)

print("satisfiable")
