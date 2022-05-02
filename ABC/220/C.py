import sys
n = int(input())
a = list(map(int, input().split()))
x = int(input())

s = [0] * len(a)

curr = 0
for i, v in enumerate(a):
    curr += v
    s[i] += curr

divisor = x // s[-1]
remainder = x % s[-1]

idx = 0
for i in range(n):
    if s[i] > remainder:
        idx = i
        break

print(divisor * n + idx + 1)