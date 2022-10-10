n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7

x = [0] * (n+1)
x[0] = 3

res = 1
for i in range(n):
    curr = a[i]
    res *= x[curr]
    res %= mod
    if x[curr]:
        x[curr] -= 1
        x[curr+1] += 1

print(res)
