s1 = input()
s2 = input()

cnt = 0
for c in s1:
    if c == "#":
        cnt += 1
for c in s2:
    if c == "#":
        cnt += 1

if cnt == 2 and (s1[0] == "#" and s2[1] == "#"):
    print("No")
elif cnt == 2 and (s1[1] == "#" and s2[0] == "#"):
    print("No")
else:
    print("Yes")