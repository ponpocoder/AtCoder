import sys
n, k = map(int, input().split())

string = []
for _ in range(n):
    string.append(input())

combinations = []

def dfs(i, curr):
    if i == n:
        combinations.append(curr.copy())
        return
    
    curr.append(string[i])
    dfs(i + 1, curr)
    curr.pop()
    dfs(i + 1, curr)

dfs(0, [])

res = 0
for comb in combinations:
    curr = 0
    dict = {i: 0 for i in range(ord("a"), ord("z") + 1)}
    for st in comb:
        for c in st:
            dict[ord(c)] += 1

    for c in dict:
        if dict[c] == k:
            curr += 1
    
    res = max(res, curr)

print(res)

