from collections import defaultdict, deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

dic = defaultdict(list)

s = []
q = deque()

for i in range(h):
    for j in range(w):
        c = a[i][j]
        if c == "S":
            q.append((i, j))
        elif c == "G" or c == ".":
            continue
        else:
            dic[c].append((i, j))

visited = [[False] * w for _ in range(h)]
used = set()
cnt = 0
while q:
    # print(q)
    for _ in range(len(q)):
        r, c = q.popleft()
        if r < 0 or r >= h or c < 0 or c >= w or a[r][c] == "#" or visited[r][c]:
            continue
        visited[r][c] = True
        curr = a[r][c]
        if curr == "G":
            print(cnt)
            exit()
        q.append((r+1, c))
        q.append((r-1, c))
        q.append((r, c+1))
        q.append((r, c-1))
        if curr != "S" and curr != "." and curr not in used:
            used.add(curr)
            for nr, nc in dic[curr]:
                if nr == r and nc == c or visited[nr][nc]:
                    continue
                q.append((nr, nc))
    cnt += 1

print(-1)
