n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

chocolate = [(a[i], b[i]) for i in range(n)]
box = [(c[i], d[i]) for i in range(m)]
chocolate.sort(reverse=True)
box.sort(reverse=True)

i, j = 0, 0
while i < n and j < m:
    if chocolate[i][0] <= box[j][0] and chocolate[i][1] <= box[j][1]:
        i += 1
    j += 1

if i == n:
    print("Yes")
else:
    print("No")
