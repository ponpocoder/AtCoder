from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

long = 0
short = 0

dic = defaultdict(int)

for v in a:
    dic[v] += 1

array = []
for i, v in dic.items():
    array.append((i, v))

array.sort(reverse=True)

for i in range(len(array)):
    x, y = array[i]
    if y >= 4 and not long:
        long = x
        short = x
        break
    elif y >= 2:
        if not long:
            long = x
        else:
            short = x
            break

print(long*short)