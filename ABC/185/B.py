n, m, t = map(int, input().split())
curr = 0
remain = n

for _ in range(m):
    a, b = map(int, input().split())
    remain -= a-curr
    # print(remain)
    if remain <= 0:
        print("No")
        exit()
    remain += b-a
    curr = b
    remain = min(n, remain)
    # print(remain)

remain -= t-curr
print("Yes" if remain > 0 else "No")
