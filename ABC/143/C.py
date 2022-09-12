n = int(input())
s = input()

cnt = 0
curr = "-1"

for i in range(n):
    if s[i] != curr:
        curr = s[i]
        cnt += 1

print(cnt)
