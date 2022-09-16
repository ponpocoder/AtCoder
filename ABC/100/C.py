n = int(input())
a = list(map(int, input().split()))

cnt = 0
for v in a:
    while v % 2 == 0:
        cnt += 1
        v //= 2

print(cnt)
