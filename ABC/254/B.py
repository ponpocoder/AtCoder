n = int(input())

a = [[1]]

for i in range(1, n):
    curr = []
    for j in range(i + 1):
        if j == 0 or j == i:
            curr.append(1)
        else:
            curr.append(a[i-1][j-1] + a[i-1][j])
    a.append(curr)

for v in a:
    print(*v)
