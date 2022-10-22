a, b = map(int, input().split())
curr = str(round(b/a, 3))

while len(curr) < 5:
    curr += "0"
print(curr)
