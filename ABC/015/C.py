n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]


def dfs(i, curr):
    if i == n:
        return curr != 0
    for j in range(k):
        if not dfs(i+1, curr ^ t[i][j]):
            return False
    return True


if dfs(0, 0):
    print("Nothing")
else:
    print("Found")
