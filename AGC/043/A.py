h, w = map(int, input().split())
s = [input() for _ in range(h)]

dp = [[float("inf")] * w for _ in range(h)]
dp[0][0] = 0 if s[0][0] == "." else 1

for r in range(h):
    for c in range(w):
        if r == 0 and c == 0:
            continue
        if s[r][c] == "#":
            curr = float("inf")
            if r > 0:
                if s[r-1][c] == ".":
                    curr = dp[r-1][c] + 1
                else:
                    curr = dp[r-1][c]
            if c > 0:
                if s[r][c-1] == ".":
                    curr = min(curr, dp[r][c-1] + 1)
                else:
                    curr = min(curr, dp[r][c-1])
        else:
            curr = float("inf")
            if r > 0:
                curr = dp[r-1][c]
            if c > 0:
                curr = min(curr, dp[r][c-1])
        dp[r][c] = curr

print(dp[-1][-1])
