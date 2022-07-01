s = input()
k = int(input())
t = set()
for i in range(len(s)):
    for j in range(1, 6):
        t.add(s[i:min(i+j, len(s))])

l = list(t)
l.sort()
print(l[k-1])