n = input()
res = 0
digit = len(n)

if digit % 2 == 1:
    res += int(n) - 10 ** (digit - 1) + 1

for i in range(digit):
    if i % 2 == 1:
        res += 9 * 10 ** (i - 1)

print(res)