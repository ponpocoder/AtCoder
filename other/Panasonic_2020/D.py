n = int(input())

def dfs(i, curr):
    if i == n:
        print("".join(curr.copy()))
        return
    
    maxChar = "a"
    for c in curr:
        if c > maxChar:
            maxChar = c
    last = chr(ord(maxChar) + 1)
    for c in range(ord("a"), ord(last) + 1):
        curr.append(chr(c))
        dfs(i + 1, curr)
        curr.pop()

dfs(1, ["a"])

