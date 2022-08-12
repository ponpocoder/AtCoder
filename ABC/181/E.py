n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
INF = 1001001001

h.sort()
w.sort()

sl = [0] * n
curr = 0 
for i in range(1, n, 2):
    curr += abs(h[i] - h[i-1])
    sl[i] = curr

sr = [0] * n
curr = 0
for i in range(n-2, -1, -2):
    curr += abs(h[i] - h[i+1])
    sr[i] = curr

print(sl)
print(sr)
res = INF

def binarySearch(i):
    target = h[i]
    l, r = 0, n-1
    while l <= r:
        m = (l+r)//2
        if w[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l

for i in range(1, m+1):
    curr = 0
    j = binarySearch(i)
    if j % 2 or j < 0 or j >= n:
        continue
    curr += abs(h[j] -w[j])
    curr += sl[j] + sr[j]
    res = min(res, curr)
    print(i, j, h[i], curr)

print(res)

