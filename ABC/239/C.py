import sys
x1, y1, x2, y2 = map(int, input().split())

nodes1 = set()
nodes2 = set()

x = [1, 1, 2, 2, -1, -1, -2, -2]
y = [2, -2, 1, -1, 2, -2, 1, -1]

for dx, dy in zip(x, y):
    nodes1.add((x1 + dx, y1 + dy))
    nodes2.add((x2 + dx, y2 + dy))

for node in nodes1:
    if node in nodes2:
        print("Yes")
        sys.exit()

print("No")