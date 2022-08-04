y = int(input())

rem = y % 4

if rem == 2:
    print(y)
elif rem == 3:
    print(y+3)
elif rem == 0:
    print(y+2)
else:
    print(y+1)
