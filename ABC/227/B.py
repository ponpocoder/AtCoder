n = int(input())
s = list(map(int, input().split()))

areas = set()

for a in range(1, 142):
    for b in range(1, 142):
        area = 4*a*b + 3*(a+b)
        if area <= 1000 and area not in areas:
            areas.add(area)

cnt = 0
for v in s:
    if v not in areas:
        cnt += 1

print(cnt)