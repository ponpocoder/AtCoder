import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = [False] * len(a)
B = [False] * len(b)
A[0] = True
B[0] = True

for i in range(n - 1):
    if (A[i] and abs(a[i + 1] - a[i]) <= k) or (B[i] and abs(a[i + 1] - b[i]) <= k):
        A[i + 1] = True
    if (A[i] and abs(b[i + 1] - a[i]) <= k) or (B[i] and abs(b[i + 1] - b[i]) <= k):
        B[i + 1] = A[i] or B[i]
    
if A[-1] or B[-1]:
    print("Yes")
else:
    print("No")