n = int(input())
mod = 998244353
pow26 = [1] * (10**6 + 1)
for i in range(10**6):
    pow26[i+1] = pow26[i] * 26 % mod

def calc():
    l = int(input())
    s = [ord(x) - ord('A') for x in input()]

    if l == 1:
        return s[0] + 1
    
    m = (l + 1) // 2

    res = 0
    for i in range(m):
        res += s[i] * pow26[m - i - 1]
        res %= mod
    
    t = [0] * l
    for i in range(m):
        t[i] = s[i]
        t[l - i - 1] = s[i]

    if t <= s:
        res += 1
        res %= mod
    
    return res

for _ in range(n):
    print(calc())