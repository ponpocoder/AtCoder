s = [list(input()) for _  in range(9)]

res = 0

for i in range(9):
    for j in range(9):
        if s[i][j] != "#":
            continue
        for k in range(j+1, 9):
            if s[i][k] != "#":
                continue
            nr = i + k - j
            if nr < 9 and s[nr][j] == "#" and s[nr][k] == "#":
                res += 1
        for k in range(j+1, 9):
            for x in range(i+1, 9):
                if s[x][k] != "#":
                    continue
                rd, cd = x-i, k-j 
                nr, nc = i+cd, j-rd
                nr2, nc2 = nr+rd, nc+cd
                # print(nr, nc, nr2, nc2, i, j, k, x)
                if nr >= 9 or nc < 0 or nr2 >= 9 or nc2 < 0 or s[nr][nc] != "#" or s[nr2][nc2] != "#":
                    continue
                res += 1

print(res)
            
