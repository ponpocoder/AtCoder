l = int(input())
res = 1
for i in range(1, 12):
    res *= l-i
    res //= i

print(res)
