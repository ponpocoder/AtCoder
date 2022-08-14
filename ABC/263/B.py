n = int(input())
p = [0] + list(map(int, input().split()))

curr = n - 1
cnt = 0
while curr != 0:
    curr = p[curr] - 1
    cnt += 1

print(cnt)
