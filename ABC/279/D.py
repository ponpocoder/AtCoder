a, b = map(int, input().split())

def calc(x):
    return b*x+a/((1+x)**0.5)

l, r = 0, 10**18

while l + 2 < r:
    m1 = (l*2+r)//3
    m2 = (l+r*2)//3

    if calc(m1) < calc(m2):
        r = m2
    else:
        l = m1

print(min(calc(l), calc(l+1), calc(r)))
