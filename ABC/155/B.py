n = int(input())
a = list(map(int, input().split()))
def check(i):
    if i % 2:
        return True
    return i % 3 == 0 or i % 5 == 0

res = True
for v in a:
    if not check(v):
        res = False
        break

print("APPROVED" if res else "DENIED")
