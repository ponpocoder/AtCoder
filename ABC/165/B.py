from math import floor

x = int(input())
curr = 100
cnt = 0
while curr < x:
    curr += curr // 100
    cnt += 1

print(cnt)
