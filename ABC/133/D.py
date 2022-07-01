n = int(input())
a = list(map(int, input().split()))
x = []
s = sum(a)

curr = s

for i in range(1, n, 2):
    curr -= 2 * a[i]    

x.append(curr)

for i in range(1, n):
    curr = 2 * a[i-1] - x[i-1] 
    x.append(curr)

print(*x)