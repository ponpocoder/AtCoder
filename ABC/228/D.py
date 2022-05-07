q = int(input())
mod = 1048576
a = [-1 for _ in range(mod)]
par = [i for i in range(mod)]


for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        h = x
        h = h % mod
        while h != par[h]:
            par[h] = par[par[h]]
            h = par[h]
        a[h] = x
        par[h] = par[(h+1)%mod]
        
    else:
        print(a[x % mod])
