n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))

print(sum(p)-max(p)//2)
