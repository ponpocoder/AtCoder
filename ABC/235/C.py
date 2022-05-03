from collections import defaultdict
n, q = map(int, input().split())

a = list(map(int, input().split()))
queries = []
dic = defaultdict(list)

for i, v in enumerate(a):
    dic[v].append(i+1)

for _ in range(q):
    x, k = map(int, input().split())
    queries.append([x, k])
    
for x, k in queries:
    if x not in dic or len(dic[x]) < k:
        print(-1)
    else:
        print(dic[x][k-1])