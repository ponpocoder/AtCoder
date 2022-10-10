s = input()
k = int(input())
n = len(s)
t = set()

for i in range(n-k+1):
    curr = s[i:i+k]
    t.add(curr)

print(len(t))
