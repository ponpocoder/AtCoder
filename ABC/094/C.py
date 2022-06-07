n = int(input())
x = list(map(int, input().split()))

sortedX = sorted(x)

first = sortedX[n // 2 - 1]
second = sortedX[n // 2]

for v in x:
    if v <= first:
        print(second)
    else:
        print(first)