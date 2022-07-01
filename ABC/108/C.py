n, k = map(int, input().split())
cnt = n // k
res = cnt**3

if k % 2 == 0:
    curr = 0
    for i in range(1, n+1):
        if i%k == k //2:
            curr += 1
    res += curr**3

print(res)