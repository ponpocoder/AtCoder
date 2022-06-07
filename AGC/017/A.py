n, p = map(int, input().split())
a = list(map(int, input().split()))

allEven = True

for v in a:
    if v % 2 != 0:
        allEven = False
        break

if allEven:
    if p == 1:
        print(0)
    else:
        print(2**n)
else:
    print(2**(n-1))