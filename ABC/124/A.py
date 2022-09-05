a, b = map(int, input().split())

if a == b:
    print(a+b)
else:
    mx = max(a, b)
    print(mx*2-1)
