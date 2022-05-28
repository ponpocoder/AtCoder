import sys
a, b, c = map(int, input().split())
k = int(input())

count = 0

while count < k:
    if b <= a:
        b *= 2
    elif c <= b:
        c *= 2
    else:
        break
    
    count += 1

if b > a and c > b:
    print("Yes")
else:
    print("No")