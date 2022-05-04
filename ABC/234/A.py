t = int(input())

def f(x):
    return x**2 + 2*x + 3

calc1 = f(t) + t
calc2 = f(calc1)
calc3 = f(f(t))
calc4 = f(calc2 + calc3)

print(calc4)