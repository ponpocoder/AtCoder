n = int(input())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

cnt = 0
for c, d in zip(a, b):
    if c >= d:
        cnt += c - d
    else:
        cnt -= (d - c) // 2

if cnt > 0:
    print("No")
else:
    print("Yes")
