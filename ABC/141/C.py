n, k, q = map(int, input().split())

cnt = [0] * n

for _ in range(q):
    a = int(input()) - 1
    cnt[a] += 1

for i in range(n):
    if k + cnt[i] - q > 0:
        print("Yes")
    else:
        print("No")
