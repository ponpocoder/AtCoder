n = int(input())
one = [0] * n
two = [0] * n

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        one[i] += p
    else:
        two[i] += p

s1 = [0] * (n + 1)
s2 = [0] * (n + 1)

for i in range(n):
    s1[i] = s1[i-1] + one[i]
    s2[i] = s2[i-1] + two[i]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(s1[r] - s1[l-1], s2[r] - s2[l-1])
