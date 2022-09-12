n = int(input())
a = list(map(int, input().split()))

par = [0] * n

for i, v in enumerate(a):
    par[v-1] += 1

for v in par:
    print(v)
