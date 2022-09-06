n = int(input())
t = 0
cost = float("inf")

for _ in range(n):
    a, p, x = map(int, input().split())
    ct = a - t
    x = max(0, x-a)
    if x:
        cost = min(cost, p)
    t = a

print(cost if cost != float("inf") else -1)
