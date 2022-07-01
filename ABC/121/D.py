a, b = map(int, input().split())

def f(x):
    cnt = (x + 1) // 2
    res = cnt % 2
    if x % 2 == 0:
        res ^= x
    return res

print(f(b)^f(a-1))