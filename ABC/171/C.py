n = int(input())

def f(n):
    if n == 0:
        return ""
    n -= 1
    return f(n//26) + chr(ord('a')+n%26)

print(f(n))