n, a, b = map(int, input().split())

white = "." * b
black = "#" * b

whites = ""
blacks = ""
for i in range(n):
    if i % 2 == 0:
        whites += white
        blacks += black
    else:
        whites += black
        blacks += white

for i in range(n):
    if i % 2 == 0:
        curr = whites
    else:
        curr = blacks
    for j in range(a):
        print(curr)