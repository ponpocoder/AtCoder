n = int(input())
a = list(map(int, input().split()))

s = set(a)
cnt = 0
while n >= 0:
    cnt += 1
    if cnt in a:
        n -= 1
    else:
        n -= 2

print(cnt-1)
