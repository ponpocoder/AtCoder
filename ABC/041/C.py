n = int(input())
a = list(map(int, input().split()))

dic = {}
for i, v in enumerate(a):
    dic[v] = i

a.sort(reverse=True)

for v in a:
    print(dic[v]+1)
