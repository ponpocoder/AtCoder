n = int(input())

chars = ["a", "b", "c"]

res = []
def dfs(i, curr):
    if i == n:
        res.append("".join(curr.copy()))
        return
    for c in chars:
        curr.append(c)
        dfs(i+1, curr)
        curr.pop()

dfs(0, [])
for re in res:
    print(re)
