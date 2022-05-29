s = input()

for i in range(len(s)-2, 0, -2):
    m = i // 2
    front = s[:m]
    back = s[m:i]

    if front == back:
        print(i)
        exit()