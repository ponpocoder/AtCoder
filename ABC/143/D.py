n = int(input())
x = list(map(int, input().split()))
x.sort()

def binarySearch(i, j):
    c = x[i] + x[j]
    l = j
    r = n - 1

    while l <= r:
        m = (l+r) // 2
        if x[m] < c:
            l = m + 1
        else:
            r = m - 1
    
    return l

res = 0
for i in range(n):
    for j in range(i+1, n):
        r = binarySearch(i, j)
        res += r - (j + 1)

print(res) 