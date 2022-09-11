n = int(input())
a = list(map(int, input().split()))

cnt = 0
res = 0

for i in range(2, 1001):
    curr = 0
    for v in a:
        if v % i == 0:
            curr += 1
    if curr > cnt:
        cnt = curr
        res = i

print(res)
