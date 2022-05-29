a, b, c = map(int, input().split())

curr = a % b
x = curr
used = set()

while x not in used:
    if x == c:
        print("YES")
        exit()
    used.add(x)
    x = (x + curr) % b

print("NO")