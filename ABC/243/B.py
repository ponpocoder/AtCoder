n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

samePositions = 0
diffPositions = 0

for i in range(n):
    for j in range(n):
        if i == j and a[i] == b[j]:
            samePositions += 1
        elif i != j and a[i] == b[j]:
            diffPositions += 1

print(samePositions)
print(diffPositions)