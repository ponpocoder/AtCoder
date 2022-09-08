from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

mp = defaultdict(int)
for i, v in enumerate(a):
    mp[v] = i + 1
    
while n > 1:
    curr =[]
    for i in range(1, 1 << n, 2):
        x = i
        y = i - 1
        curr.append(max(a[x], a[y]))
    a = curr
    n -= 1

print(mp[min(a)])
