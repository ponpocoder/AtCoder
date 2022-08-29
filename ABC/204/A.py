x, y = map(int, input().split())
s = set()
s.add(x)
s.add(y)
if len(s) == 1:
    print(x)
elif 0 not in s:
    print(0)
elif 1 not in s:
    print(1)
else:
    print(2)
