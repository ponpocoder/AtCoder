n = int(input())

b = int(n**0.5)
res = 0

for i in range(1, b+1):
    res += n // i

res += res - b**2 
print(res)
