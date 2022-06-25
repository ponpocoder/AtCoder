n, x = map(int, input().split())

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = x //n - 1
if x % n:
    i += 1
print(s[i])