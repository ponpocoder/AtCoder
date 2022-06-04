n, k = map(int, input().split())
a = list(map(int, input().split()))

x = []
for i in range(k):
    curr = []
    for j in range(i, n, k):
        curr.append(a[j])
    curr.sort()
    x.append(curr)

for i in range(len(x[0])):
    for j in range(1, k):
        if i >= len(x[j]):
            break
        if x[j][i] < x[j-1][i]:
            print("No")
            exit()

print("Yes")