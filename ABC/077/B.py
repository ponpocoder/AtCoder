n = int(input())
res = 1
for i in range(1, n):
    curr = i * i
    if curr > n:
        break
    res = curr

print(res) 
