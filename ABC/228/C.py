n, k = map(int, input().split())
s = []

for _ in range(n):
    a, b, c = map(int, input().split())
    curr = a + b + c
    s.append(curr)

t = sorted(s)
b = t[n - k]

for score in s:
    if score + 300 >= b:
        print("Yes")
    else:
        print("No")