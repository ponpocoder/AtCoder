s = input()
odd = "RUD"
even = "LUD"

for i, c in enumerate(s):
    if (i % 2 == 0 and c not in odd) or (i % 2 and c not in even):
        print("No")
        exit()

print("Yes")
