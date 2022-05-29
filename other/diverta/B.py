r, g, b, n = map(int, input().split())

l = n // r
m = n // g
o = n // b

res = 0
for i in range(l+1):
    for j in range(m+1):
        remain = n - (r*i+g*j)
        if 0 <= remain // b <= o and remain % b == 0:
            res += 1

print(res)