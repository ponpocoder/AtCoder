n = int(input())
s = set()

flag = True
for i in range(n):
    x = input()
    a = x[0]
    b = x[1]
    if a not in ["H", "D", "C", "S"]:
        flag = False
    if b not in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]:
        flag = False
    s.add(x)

if len(s) != n:
    flag = False

print("Yes" if flag else "No")
