n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
c.sort()

def binarySearch(d, target, isLeft):
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if d[m] == target:
            if isLeft:          
                r = m - 1
            else:
                l = m + 1
        elif d[m] < target:
            l = m + 1
        else:
            r = m - 1
            
    return l

res = 0
for i in range(n):
    l = binarySearch(a, b[i], True)
    r = n - binarySearch(c, b[i], False)
    res += l * r 

print(res)

