a, b = map(int, input().split())

for i in range(1, 10000):
    x = i * 8 // 100
    y = i * 10 // 100
    if x == a and y == b:
        print(i)
        exit()
