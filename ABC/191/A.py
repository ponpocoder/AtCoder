v, t, s, d = map(int, input().split())

if d < v * t:
    print("Yes")
elif d > v * s:
    print("Yes")
else:
    print("No")
