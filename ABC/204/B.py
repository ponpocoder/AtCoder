n = int(input())
a = list(map(int, input().split()))

cnt = 0

for v in a:
    if v > 10:
        cnt += v - 10

print(cnt)
