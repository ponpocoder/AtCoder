s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

p1 , p2 = 0, 0

for i in range(min(len(s), len(t))):
    if s[i] > t[i]:
        print("No")
        exit()
    elif s[i] < t[i]:
        print("Yes")
        exit()

if len(s) < len(t):
    print("Yes")
else:
    print("No")