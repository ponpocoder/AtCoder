n = int(input())

for i in range(1, 10**6+1):
    if int(str(i)*2) > n:
        print(i-1)
        exit()
