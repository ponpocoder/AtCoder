from collections import defaultdict
import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic = defaultdict(int)

for v in a:
    dic[v] += 1

i = 0

for v in b:
    if dic[v] == 0:
        print("No")
        sys.exit()
    dic[v] -= 1
    i += 1

print("Yes")