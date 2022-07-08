s, t = map(int, input().split())
u, v = map(int, input().split())

res = 0
if s == u and t == v:
    res = 0
elif s + t == u + v:
    res = 1
elif s - t == u - v:
    res = 1
elif abs(s-u) + abs(t-v) <= 3:
    res = 1
elif (s+t)%2 == (u+v)%2:
    res = 2
elif abs(s-u)+abs(t-v)<=6:
    res = 2
elif abs((s+t)-(u+v))<=3:
    res = 2
elif abs((s-t)-(u-v))<=3:
    res = 2
else:
    res = 3

print(res)