n = int(input())
A = []
B = []
T = []

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(a / b)

seconds = 0

for t in T:
    seconds += t  
    
remain = seconds / 2

res = 0
i = 0
while remain > 0:
    if remain >= T[i]:
        res += A[i]
        remain -= T[i]
    else:
        res += remain * B[i]
        remain = 0
    i += 1

print(res)