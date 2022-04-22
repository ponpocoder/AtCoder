x = int(input())

count = 0
while x >= 100:
    x -= 100
    count += 1

if x <= count * 5:
    print(1)
else:
    print(0)