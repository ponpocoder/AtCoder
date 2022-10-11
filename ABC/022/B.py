n = int(input())
s = set()
cnt = 0
for _ in range(n):
    a = int(input())
    if a in s:
        cnt += 1
    s.add(a)

print(cnt)
