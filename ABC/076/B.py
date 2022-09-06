n = int(input())
k = int(input())

curr = 1

for _ in range(n):
    curr = min(curr*2, curr+k)

print(curr)
