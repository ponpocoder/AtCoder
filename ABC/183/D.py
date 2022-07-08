n, w = map(int, input().split())
x = [0] * (2*10**5+1)
y = [w*i for i in range(2*10**5+1)]
for _ in range(n):
    s, t, p = map(int, input().split())
    x[s] += p
    x[t] -= p
    # print(x[:10])

curr = 0
for i in range(n+1):
    curr += x[i]
    if curr > w:
        print("No")
        exit()

print("Yes")