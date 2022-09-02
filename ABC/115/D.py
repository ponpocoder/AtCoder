n, x = map(int, input().split())

a = [1]
b = [1]

for i in range(n):
    a.append(a[-1]*2 + 3)
    b.append(b[-1]*2 + 1)


def f(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n-1]:
        return f(n-1, x-1)
    else:
        return b[n-1] + 1 + f(n-1, x - 2 - a[n-1])


print(f(n, x))
