import sys

n = int(input())
a = list(map(int, input().split()))

values = set()
for v in a:
    values.add(v)

for i in range(n + 1):
    if i not in values:
        print(i)
        sys.exit()