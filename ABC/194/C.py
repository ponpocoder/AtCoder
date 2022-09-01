n = int(input())
a = list(map(int, input().split()))

A = 200
b = [0] * (A*2+1)

res = 0
for i in range(n):
    for j in range(-A, A+1):
        cnt = b[A+j]
        curr = a[i] - j
        res += cnt * curr * curr
    b[A+a[i]] += 1

print(res)
