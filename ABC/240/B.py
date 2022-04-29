n = int(input())
a = list(map(int, input().split()))

values = set()

for v in a:
    values.add(v)

print(len(values))