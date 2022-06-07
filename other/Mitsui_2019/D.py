n = int(input())
s = input()
passwords = set()
res = 0

for i in range(1000):
    strI = str(i).zfill(3)
    idx = 0
    for j in range(len(s)):
        if s[j] == strI[idx]:
            idx += 1
        if idx == 3:
            res += 1
            break
print(res)
