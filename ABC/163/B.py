n, m = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)

remain = n-s
print(remain if remain >= 0 else -1)
