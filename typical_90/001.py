n, l = map(int, input().split())
k = int(input())
positions = list(map(int, input().split()))

def isValid(m):
    count = 0
    prev = 0
    for i in range(n):
        if positions[i] - prev >= m:
            count += 1
            prev = positions[i]
    
    if l - prev >= m:
        count += 1
    return count >= k + 1

left, right = 0, l
res = 0
while left <= right:
    middle = (left + right) // 2
    if isValid(middle):
        res = middle
        left = middle + 1
    else:
        right = middle - 1

print(res)