from collections import defaultdict

s = input()
dic = defaultdict(int)

for c in s:
    dic[c] += 1

for v in dic.values():
    if v != 2:
        print("No")
        exit()

print("Yes")
