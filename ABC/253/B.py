h, w = map(int, input().split())
s = [input() for _ in range(h)]

first = [-1, -1]
for i in range(h):
    for j in range(w):
        if s[i][j] == "o":
            if first == [-1, -1]:
                first = [i, j]
            else:
                d = abs(first[0] - i) + abs(first[1] - j)
                print(d)
                exit()
        
