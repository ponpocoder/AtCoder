sa = input()
sb = input()
sc = input()
p1, p2, p3 = 0, 0, 0
curr = "a"
while p1 <= len(sa) and p2 <= len(sb) and p3 <= len(sc):
    if curr == "a":
        if p1 == len(sa):
            print("A")
            exit()
        curr = sa[p1]
        p1 += 1
    elif curr == "b":
        if p2 == len(sb):
            print("B")
            exit()
        curr = sb[p2]
        p2 += 1
    else:
        if p3 == len(sc):
            print("C")
            exit()
        curr = sc[p3]
        p3 += 1