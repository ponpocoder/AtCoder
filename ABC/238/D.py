t = int(input())
results = []
for _ in range(t):
    a, s = map(int, input().split())
    if s >= 2 * a and (s - 2 * a) & a == 0:
        results.append("Yes")
    else:
        results.append("No")

for res in results:
    print(res)