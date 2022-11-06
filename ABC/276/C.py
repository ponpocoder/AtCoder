n = int(input())
p = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    for j in reversed(range(i+1, n)):
        if p[i] > p[j]:
            p[i], p[j] = p[j], p[i]
            x = p[i+1:]
            x.sort(reverse=True)
            res = p[:i+1] + x
            print(*res)
            exit()
