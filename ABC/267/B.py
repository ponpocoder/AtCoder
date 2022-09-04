s = input()

r = [0] * 7
for i, c in enumerate(s):
    if c == "0":
        continue
    if i == 0 or i == 4:
        r[3] += 1
    if i == 1 or i == 7:
        r[2] += 1
    if i == 2 or i == 8:
        r[4] += 1
    if i == 3:
        r[1] += 1
    if i == 6:
        r[0] += 1
    if i == 5:
        r[5] += 1
    if i == 9:
        r[6] += 1

if s[0] != "0":
    print("No")
    exit()

for i in range(6):
    if r[i] == 0:
        continue
    if r[i+1] != 0:
        continue
    for j in range(i+2, 7):
        if r[j] != 0:
            print("Yes")
            exit()

print("No")
