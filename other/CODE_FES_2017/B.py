from collections import defaultdict

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

dic = defaultdict(int)

for v in d:
    dic[v] += 1

for v in t:
    dic[v] -= 1
    if dic[v] < 0:
        print("NO")
        exit()

print("YES")