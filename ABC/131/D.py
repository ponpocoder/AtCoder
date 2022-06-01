n = int(input())
a = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x:x[1])
curr = 0

for i in range(n):
    x, y = a[i]
    curr += x
    if curr > y:
        print("No")
        exit()

print("Yes")