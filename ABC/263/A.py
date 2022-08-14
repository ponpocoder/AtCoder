from collections import defaultdict

a, b, c, d, e = map(int, input().split())
dic = defaultdict(int)

dic[a] += 1
dic[b] += 1
dic[c] += 1
dic[d] += 1
dic[e] += 1

two = False
three = False
for v in dic.values():
    if v == 2:
        two = True
    if v == 3:
        three = True

if two and three:
    print("Yes")
else:
    print("No")
