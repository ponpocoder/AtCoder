n = int(input())

res = n // 100
if n % 100:
    res += 1
print(res)
