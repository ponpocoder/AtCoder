n = int(input())

cnt = 0

for a in range(1, n+1):
    if a*a*a > n:
        break
    for b in range(a, n+1):
        if a*b*b > n:
            break
        
        macC = n // (a*b)
        cnt += macC - b + 1

print(cnt)