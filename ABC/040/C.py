n = int(input())
a = list(map(int, input().split()))

one = 0
two = abs(a[1] - a[0])

for i in range(2, n):
    tmp = two
    two = min(one + abs(a[i]-a[i-2]), two + abs(a[i]-a[i-1]))
    one = tmp

print(two)
