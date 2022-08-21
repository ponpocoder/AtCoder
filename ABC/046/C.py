n = int(input())

x, y = 1, 1
for _ in range(n):
    t, a = map(int, input().split())
    n = max((x+t-1)//t, (y+a-1)//a)
    x = n * t
    y = n * a

print(x+y)
