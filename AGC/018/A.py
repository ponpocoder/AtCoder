from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))

curr = a[0]
for v in a:
    curr = gcd(curr, v)

if max(a) >= k and k % curr == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")