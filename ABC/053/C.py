x = int(input())

res = x // 11 * 2
if 0 < x % 11 <= 6:
    res += 1
elif x % 11 > 6:
    res += 2 

print(res)