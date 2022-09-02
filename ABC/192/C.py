n, k = map(int, input().split())


def f(x):
    digit = []
    while x:
        digit.append(x % 10)
        x //= 10

    digit.sort()

    small = 0
    for i in range(len(digit)):
        small *= 10
        small += digit[i]

    large = 0
    for i in range(len(digit)-1, -1, -1):
        large *= 10
        large += digit[i]

    return large - small


a = n
for _ in range(k):
    a = f(a)
print(a)
