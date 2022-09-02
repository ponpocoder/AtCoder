x = int(input())

for i in range(1, 1000):
    a = i ** 5
    for j in range(-1000, 1000):
        b = j ** 5
        if (a - b == x):
            print(i, j)
            exit()
