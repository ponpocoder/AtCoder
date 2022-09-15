n, k = map(int, input().split())
mod = 10**9 + 7

res = 0

def calc(l, r):
    return  (l+r)*(r-l+1)//2

for i in range(k, n+2):
    l = calc(0, i-1)
    r = calc(n-i+1, n)
    res += r - l + 1
    res %= mod

print(res)
    
