x, k = map(int, input().split())

for i in range(k):
    curr = 10 ** (i+1)
    if x % curr >= 5*10**i:
        x += 10**(i+1)
    x -= x % curr

print(x)
