x = int(input())
res = 0
for i in range(1, x+1):
    s = i * (i+1) // 2
    res = i
    if s >= x:
        break

print(res)    
