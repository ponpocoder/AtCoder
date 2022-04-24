    from collections import deque
    import sys
    row, col = map(int, input().split())

    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    matrix = []
    for _ in range(row):
        line = input()
        matrix.append(line)

    q = deque()
    q.append((sy - 1, sx - 1))
    visited = set()
    curr = 0

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if r < 0 or r >= row or c < 0 or c >= col or matrix[r][c] == "#" or (r, c) in visited:
                continue
            visited.add((r, c))
            if r == gy - 1 and c == gx - 1:
                print(curr)
                sys.exit()
            q.append((r + 1, c))
            q.append((r - 1, c))
            q.append((r, c + 1))
            q.append((r, c - 1))
        curr += 1
        