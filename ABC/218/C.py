import sys

n = int(input())
s = set()
t = set()

for y in range(n):
    curr = input()
    for x in range(n):
        if curr[x] == "#":
            s.add((x, y))

for y in range(n):
    curr = input()
    for x in range(n):
        if curr[x] == "#":
            t.add((x, y))           

for _ in range(4):
    minX, minY = min(s)
    s = set((x - minX, y - minY) for x, y in s) 
    minX, minY = min(t)
    t = set((x - minX, y - minY) for x, y in t) 
    if s == t:
        print("Yes")
        sys.exit()

    s = set((y, - x) for x, y in s)

print("No")