n = int(input())
h = list(map(int, input().split()))

res = 0
curr = 0

for i in range(n):
    if h[i] > curr:
        curr = h[i]
        res = i

print(res+1)
