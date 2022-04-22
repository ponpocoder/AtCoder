n, m, q = map(int, input().split())
a, b, c, d = [], [], [], []

for _ in range(q):
    inputs = list(map(int, input().split()))
    a.append(inputs[0])
    b.append(inputs[1])
    c.append(inputs[2])
    d.append(inputs[3])

A = [0] * n
res = 0
def dfs(i, j): #i:index, j:value
    if i == len(A):
        curr = 0
        for x, y, z, w in zip(a, b, c, d):
            if A[y - 1] - A[x - 1] == z:
                curr += w
        global res
        res = max(curr, res)
        return
    
    A[i] = j
    for k in range(j, m + 1):
        dfs(i+1, k)

dfs(0, 1)
print(res)
