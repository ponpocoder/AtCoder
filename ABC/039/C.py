s = input()
s = s[:12]

t = "WBWBWWBWBWBW"
res = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]

for i in range(12):
    if t == s:
        print(res[i])
        exit()
    t = t[1:] + t[0]
