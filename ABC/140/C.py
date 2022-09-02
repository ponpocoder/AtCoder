n = int(input())
b = list(map(int, input().split()))

res = b[-1]
for i in range(n-1):
    if i == 0:
        res += b[i]
    else:
        res += min(b[i], b[i-1])

print(res)
