n, q = map(int, input().split())

both = set()
one = set()
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        one.add((a, b))
        if (b, a) in one:
            both.add((a, b))
            both.add((b, a))
    elif t == 2:
        if (a, b) in one:
            one.remove((a, b))
        if (a, b) in both:
            both.remove((a, b))
            both.remove((b, a))
    else:
        if (a, b) in both:
            print("Yes")
        else:
            print("No")
