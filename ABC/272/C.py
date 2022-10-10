n = int(input())
a = list(map(int, input().split()))

a.sort()

firstOdd = -1
secondOdd = -1
firstEven = -1
secondEven = -1

for i in range(n-1, -1, -1):
    if a[i] % 2:
        if secondOdd != -1:
            continue
        if firstOdd != -1:
            secondOdd = a[i]
        else:
            firstOdd = a[i]
    else:
        if secondEven != -1:
            continue
        if firstEven != -1:
            secondEven = a[i]
        else:
            firstEven = a[i]

even = -1
odd = -1
if firstOdd != -1 and secondOdd != -1:
    odd = firstOdd + secondOdd
if firstEven != -1 and secondEven != -1:
    even = firstEven + secondEven

mx = max(odd, even)

print(mx)
