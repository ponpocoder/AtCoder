v, a, b, c = map(int,input().split())

while v >= 0:
    if v < a:
        print("F")
    elif v < a + b:
        print("M")
    elif v < a + b + c:
        print("T")
    v -= a + b + c