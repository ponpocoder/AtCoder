n = int(input())
res = 0

def dfs(curr, use3, use5, use7):
    if int(curr) > n:
        return
    if use3 and use5 and use7:
        global res
        res += 1
    dfs(curr+"3", True, use5, use7)
    dfs(curr+"5", use3, True, use7)
    dfs(curr+"7", use3, use5, True)

dfs("0", False, False, False)
print(res)