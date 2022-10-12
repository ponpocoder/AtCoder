n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def dfs(i, curr, cnt, friends, visited):
    x = 0
    if cnt == 1:
        for friend in graph[i]:
            friends.add(friend)
        for friend in graph[i]:
            x += dfs(i, friend, cnt-1, friends, visited)
        return x
    else:
        for friend in graph[curr]:
            if i == friend or friend in friends or friend in visited:
                continue
            x += 1
            visited.add(friend)
        return x


for i in range(n):
    print(dfs(i, i, 1, set(), set()))
