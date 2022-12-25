from collections import defaultdict

k = int(input())
l, r = 0, 10**12
mp = defaultdict(int)

curr = k
for i in range(2, k+1):
    if i*i > k:
        break
    if curr % i == 0:
        cnt = 0
        while curr % i == 0:
            curr //= i
            cnt += 1
        mp[i] = cnt

if curr > 1:
    mp[curr] = 1

def f(x, y):
    if x == 0:
        return 0
    return x//y + f(x//y, y)

def judge(x):
    for key, value in mp.items():
        if f(x, key) < value:
            return False
    return True

while l + 1 < r:
    m = (l+r)//2
    if judge(m):
        r = m
    else:
        l = m

print(r)
