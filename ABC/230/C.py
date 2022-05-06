n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
n -= 1
a -= 1
b -= 1
p -= 1
q -= 1
r -= 1
s -= 1

lower1 = max(1 - a, 1 - b)
upper1 = min(n - a, n - b)
lower2 = max(1 - a, b - n)
upper2 = min(n - a, b - 1)

inBounds = set()

def isInside(r, c):
    return (r + c) == a + b or (r - c) == a - b

for i in range(p, q+1):
    curr = []
    for j in range(r, s + 1):
        if isInside(i, j):
            curr.append("#")
        else:
            curr.append(".")
    print("".join(curr))
