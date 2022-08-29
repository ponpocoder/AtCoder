n = int(input())
m = []

for _ in range(n):
    s, t = input().split()
    m.append((int(t), s))

m.sort(reverse=True)

print(m[1][1])
