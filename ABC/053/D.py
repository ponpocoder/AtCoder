from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dic = defaultdict(int)

for v in a:
    dic[v] += 1
    if dic[v] == 3:
        dic[v] = 1

one = 0
two = 0
# print(dic)

for i, v in dic.items():
    if v == 1:
        one += 1
    elif v == 2:
        two += 1

if two % 2 == 0:
    print(one + two) 
else:
    print(one + two - 1)