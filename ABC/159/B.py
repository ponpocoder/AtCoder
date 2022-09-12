s = input()
n = len(s)


def isPali(x):
    l, r = 0, len(x) - 1

    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True


if isPali(s) and isPali(s[:(n-1)//2]) and isPali(s[(n+3)//2-1:]):
    print("Yes")
else:
    print("No")
