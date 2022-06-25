n, k, q = map(int, input().split())
a = set(map(int, input().split()))
l = list(map(int, input().split()))

b = list(a)
b.sort()

for v in l:
    v -= 1
    if v == k - 1 and b[v] == n:
        continue
    elif v < k - 1 and b[v+1] == b[v] + 1:
        continue
    else:
        b[v] += 1

print(*b)