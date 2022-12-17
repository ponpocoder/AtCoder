n, t = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)

t %= s

curr = 0

for i in range(n):
    if curr + a[i] >= t:
        print(i+1, t-curr)
        exit()
    curr += a[i]
