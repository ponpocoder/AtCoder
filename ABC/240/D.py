n = int(input())
a = list(map(int, input().split()))

stack = []

for num in a:
    if stack:
        last = stack[-1]
        if last[0] == num:
            if last[1] == num - 1:
                for _ in range(num - 1):
                    stack.pop()
            else:
                stack.append((num, last[1] + 1))
        else:
            stack.append((num, 1))
    else:
        stack.append((num, 1))    
    print(len(stack))


    