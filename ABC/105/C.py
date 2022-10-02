n = int(input())

curr = 1
while curr * 2 < n:
    curr *= 2

res = ""
while n != 0:
    print(n)
    if n % 2:
        n -= 1
        res = "1" + res
    else:
        res = "0" + res
    n //= -2

if res == "":
    res = "0"

print(res)
