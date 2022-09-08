n, x = map(int, input().split())
curr = 0
for i in range(n):
    v, p = map(int, input().split())
    curr += v * p 
    if curr > x * 100:
        print(i+1)
        exit()

print(-1)
