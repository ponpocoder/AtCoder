n = int(input())


def getCount(i):
    count = 0
    while i % 2 == 0:
        i /= 2
        count += 1
    return count


maxCount = 0
res = 1
for i in range(1, n + 1):
    count = getCount(i) 
    if count > maxCount:
        maxCount = count
        res = i

print(res)
