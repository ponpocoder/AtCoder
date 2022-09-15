n = int(input())
a = list(map(int, input().split()))

cnt = 0
for v in a:
    if v % 2 == 0:
        while v % 2 == 0:
            cnt += 1
            v //= 2

print(cnt)
