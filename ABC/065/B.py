n = int(input())
a = []
for _ in range(n):
    a.append(int(input()) - 1)

visited = [False] * n
curr = 0
cnt = 0
while not visited[curr]:
    visited[curr] = True
    if curr == 1:
        print(cnt)
        exit()
    
    curr = a[curr]
    cnt += 1

print(-1)