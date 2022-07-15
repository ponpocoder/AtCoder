n = int(input())
a = list(map(int, input().split()))
A = 1000001
cnt = [0] * A

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

for v in a:
    cnt[v] += 1

pairwise = True
for i in range(2, A):
    c = 0
    for j in range(i, A, i):
        c += cnt[j]
    if c > 1:
        pairwise = False
        break

if pairwise:
    print("pairwise coprime")
    exit()

x = 0
for v in a:
    x = gcd(x, v)

if x == 1:
    print("setwise coprime")
    exit()

print("not coprime")
