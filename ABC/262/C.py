n = int(input())
a = list(map(int, input().split()))

res = 0
cnt = 0
for i in range(n):
    if a[i] != i + 1:
        if a[a[i]-1] == i+1:
            res += 1
    else:
        cnt += 1
res //= 2
res += cnt*(cnt-1)//2
print(res)
