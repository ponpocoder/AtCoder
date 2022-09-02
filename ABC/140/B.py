n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

res = 0
for i in range(n):
    curr = a[i] - 1
    res += b[curr]
    if i > 0 and a[i-1] + 1 == a[i]:
        res += c[curr-1]

print(res)
