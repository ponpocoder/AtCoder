n = int(input())
children = [[] for _ in range(n)]

for i in range(n-1):
    b = int(input())
    children[b-1].append(i+1)


def dfs(i):
    if len(children[i]) == 0:
        return 1
    cnt = []
    for j in children[i]:
        cnt.append(dfs(j))
    return max(cnt)+min(cnt)+1


print(dfs(0))
