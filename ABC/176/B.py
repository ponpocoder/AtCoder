n = input()

curr = 0

for i in range(len(n)-1, -1, -1):
    curr += int(n[i])

if curr % 9 == 0:
    print("Yes")
else:
    print("No")
