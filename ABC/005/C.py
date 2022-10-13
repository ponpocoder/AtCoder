t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = 0
j = 0

while i < n and j < m:
    if a[i] <= b[j] <= a[i] + t:
        j += 1
    i += 1

print("yes" if j == m else "no")
