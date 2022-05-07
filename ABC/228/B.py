n, x = map(int, input().split())
a = list(map(int, input().split()))

known = [False] * n

cnt = 0
curr = x - 1

while not known[curr]:
    known[curr] = True
    curr = a[curr] - 1
    cnt += 1

print(cnt)
