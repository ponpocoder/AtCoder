n = int(input())
a = list(map(int, input().split()))

curr = 1
cnt = 0
for v in a:
    if v != curr:
        cnt += 1
    else:
        curr += 1

print(cnt if cnt != n else -1)
