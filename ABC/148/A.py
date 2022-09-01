a = int(input())
b = int(input())

s = set()
s.add(a)
s.add(b)

for i in range(1, 4):
    if i not in s:
        print(i)
        exit()
