n = int(input())
curr = 0
res = 0
for i in range(1, n+1):
    curr += i
    if curr >= n:
        res = i
        break

remain = curr - n

for i in range(1, res + 1):
    if i == remain:
        continue
    print(i)