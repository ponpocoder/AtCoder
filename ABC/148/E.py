n = int(input())

if n % 2 == 1:
    print(0)
    exit()

n = n // 2

curr = 5
res = 0

while curr <= n:
    res += n // curr
    curr *= 5

print(res)