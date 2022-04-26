from re import L


n, x = map(int, input().split())
s = input()
stack = []

for c in s:
    if c == "U":
        if stack and stack[-1] != "U":
            stack.pop()
        else:
            stack.append("U")
    else:
        stack.append(c)

s = "".join(stack)
for c in s:
    if c == "U":
        x = x // 2 
    elif c == "L":
        x *= 2
    else:
        x = x * 2 + 1
print(x)