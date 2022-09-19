n = int(input())
a = list(map(int, input().split()))

curr = 1

for v in a:
    if v == 0:
        print(0)
        exit()

for v in a:
    curr *= v
    if curr > 10**18:
        print(-1)
        exit()

print(curr)
