s, t, x = map(int, input().split())

if t > s:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
else:
    if x >= s or x < t:
        print("Yes")
    else:
        print("No")