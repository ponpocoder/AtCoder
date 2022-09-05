a, b = map(int, input().split())

s = a + b

if s % 2:
    print("IMPOSSIBLE")
else:
    print(s//2)
