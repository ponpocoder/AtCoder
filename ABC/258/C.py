n, q = map(int, input().split())
s = list(input())
curr = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        curr += x
        curr %= len(s)
    else:
        print(s[-curr+x-1])