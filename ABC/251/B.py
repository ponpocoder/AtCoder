n, w = map(int, input().split())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] <= w:
        s.add(a[i])
    for j in range(i+1, n):
        if a[i] + a[j] <= w:
            s.add(a[i] + a[j])
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= w:
                s.add(a[i] + a[j] + a[k])
print(len(s))
