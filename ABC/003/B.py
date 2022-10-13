s = input()
t = input()

for a, b in zip(s, t):
    if a == b:
        continue
    if a == "@" and b in ["a", "t", "c", "o", "d", "e", "r"]:
        continue
    if b == "@" and a in ["a", "t", "c", "o", "d", "e", "r"]:
        continue
    print("You will lose")
    exit()

print("You can win")
