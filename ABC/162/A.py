n = int(input())

while n:
    if n % 10 == 7:
        print("Yes")
        exit()
    n //= 10

print("No")
