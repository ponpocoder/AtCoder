h = int(input())


def dfs(i):
    if i == 1:
        return 1
    return 2 * dfs(i//2) + 1


print(dfs(h))
