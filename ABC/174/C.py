import sys
k = int(input())

a = [0] * k
a[0] = 7 % k

for i in range(1, k):
    a[i] = (a[i-1]*10 + 7) % k

for i in range(k):
    if a[i] == 0:
        print(i+1)
        sys.exit()

print(-1)