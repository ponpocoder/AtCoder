n = int(input())
p = list(map(int, input().split()))

cnt = 0
idx = -1
res = True
for i in range(n):
    if i+1 != p[i]:
        if cnt == 0:
            idx = i
            cnt += 1
        elif cnt == 1:
            if idx + 1 == p[i] and i + 1 == p[idx]:
                cnt += 1
            else:
                res = False
        else:
            res = False

print("YES" if res else "NO")
