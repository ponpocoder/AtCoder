h, n = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)

print("Yes" if s >= h else "No")
