s = input()
k = int(input())

for i in range(len(s)):
    if s[i] == "1":
        if k == i + 1:
            print(s[i])
            exit()
    else:
        print(s[i])
        exit()