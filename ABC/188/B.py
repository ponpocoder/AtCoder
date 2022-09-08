n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

curr = 0
for x, y in zip(a, b):
    curr += x * y

print("Yes" if curr == 0 else "No")
