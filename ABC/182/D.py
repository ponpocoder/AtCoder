n = int(input())
a = list(map(int, input().split()))

mx = 0
curr = 0
x = 0
b = 0
res = 0
for v in a:
    b += v
    mx = max(mx, b)
    res = max(res, x+mx)
    curr += v
    x += curr

print(res)