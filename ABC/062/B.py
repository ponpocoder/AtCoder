h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

x = []
x.append("#"*(w+2))
for r in a:
    x.append(["#"] + r + ["#"])
x.append("#"*(w+2))

for r in x:
    print("".join(r))
