n = int(input())


def dfs(open, close, curr):
    if open == close == 0:
        print(curr)
        return

    if open > 0:
        new = curr + "("
        dfs(open - 1, close, new)

    if close > open:
        new = curr + ")"
        dfs(open, close - 1, new)


if n & 1 == 0:
    dfs(n / 2, n / 2, "")
else:
    pass

