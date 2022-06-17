x = input()
stack = []

for c in x:
    if c == "S":
        stack.append(c)
    else:
        if stack and stack[-1] == "S":
            stack.pop()
        else:
            stack.append(c)

print(len(stack))