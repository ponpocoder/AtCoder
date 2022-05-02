n, m = map(int, input().split())

s = list(input().split())
t = set(input().split())

for a in s:
    if a in t:
        print("Yes")
    else:
        print("No")