s = input()
cnt = 0

for c in s:
    if c == 'v':
        cnt += 1
    elif c == 'w':
        cnt += 2
print(cnt)
