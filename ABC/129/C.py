n, m = map(int, input().split())
broken = [False] * (n+1)
mod = 10**9+7
for _ in range(m):
    a = int(input())
    broken[a] = True

one, two = 1, 1

if broken[1]:
    two = 0

for i in range(2, n+1):
    if broken[i]:
        one = two
        two = 0
    else:
        tmp = two
        two = (one + two) % mod
        one = tmp

print(two)