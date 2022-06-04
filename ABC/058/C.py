n = int(input())

curr = set(list(input()))
for _ in range(1, n):
    s = set(list(input()))
    print(s, curr)
    curr = curr & s

res = list(curr)
res.sort()
print("".join(res))