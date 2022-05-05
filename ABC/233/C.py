n, x = map(int, input().split())

bags = []
for _ in range(n):
    inputs = list(map(int, input().split()))
    bags.append(inputs[1:])

cnt = 0
def dfs(i, curr):
    if i == n:
        if curr == x:
            global cnt
            cnt += 1
        return
    for ball in bags[i]:
        dfs(i+1, curr*ball)

dfs(0, 1)
print(cnt)


