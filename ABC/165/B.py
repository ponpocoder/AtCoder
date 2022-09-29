from math import floor

x = int(input())
curr = 100
cnt = 0
while curr < x:
    curr *= 1.01
    curr = floor(curr)
    cnt += 1

print(cnt)
