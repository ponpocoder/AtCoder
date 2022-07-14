from calendar import c


n, x, m = map(int, input().split())

id = [-1] * m
memo = []

idx = 0
curr = x
while id[x] == -1:
    memo.append(x)
    id[x] = idx
    idx += 1
    x = x ** 2 % m

one = id[x]
two = idx - id[x]
# print(memo)
# print(one, two)

res = 0
if n <= one:
    for i in range(n):
        res += memo[i]
else:
    for i in range(one):
        res += memo[i]
    cycle = 0
    for i in range(one, idx):
        cycle += memo[i]
    
    div = (n-one) // two
    rem = (n-one) % two
    
    # print(cycle, div, rem)
    res += cycle * div
    for i in range(one, one+rem):
        res += memo[i]

print(res)