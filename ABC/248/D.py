from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
q = int(input())
indecies = defaultdict(list)

for i, a in enumerate(a):
    indecies[a].append(i)

def leftBinarySearch(left, array):
    i = - 1
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] >= left:
            i = m
            r = m - 1
        else:
            l = m + 1
    return i

def rightBinarySearch(right, array):
    i = - 1
    l, r = 0, len(array) - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] <= right:
            i = m
            l = m + 1
        else:
            r = m - 1
    return i

for _ in range(q):
    l, r, x = map(int, input().split())
    left = leftBinarySearch(l - 1, indecies[x])
    right = rightBinarySearch(r - 1, indecies[x])
    if left == -1 or right == -1:
        print(0)
    else:
        print(right - left + 1)