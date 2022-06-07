n = int(input())
a = list(map(int, input().split()))

four = 0
two = 0
one = 0

for v in a:
    if v % 4 == 0:
        four += 1
    elif v % 2 == 0:
        two += 1
    else:
        one += 1


if two == 0:
    if four + 1 >= one:
        print("Yes")
    else:
        print("No")
else:
    if four >= one:
        print("Yes")
    else:
        print("No")