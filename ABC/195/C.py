n = int(input())

x = 1000
cnt = 0
while n >= x:
    cnt += n - x + 1
    x *= 1000

print(cnt)
