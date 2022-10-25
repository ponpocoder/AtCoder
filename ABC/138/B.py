n = int(input())
a = list(map(int, input().split()))

y = 1

for v in a:
    y *= v

s = 0
for v in a:
    s += y // v
    
print(y/s)
