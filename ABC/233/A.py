x, y = map(int, input().split())

remain = y - x
cnt = 0
while remain > 0:
    remain -= 10
    cnt += 1

print(cnt)