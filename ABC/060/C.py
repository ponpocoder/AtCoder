n, t = map(int, input().split())
a = list(map(int, input().split()))

res = 0
curr = t
diff = [t]

for i in range(1, n):
    d = a[i] - a[i-1]
    diff.append(d)

for i in range(n):
    if diff[i] < t:
        res += diff[i]
    else:
        res += t

print(res)