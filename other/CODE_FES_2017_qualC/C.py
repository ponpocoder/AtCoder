s = input()

l, r = 0, len(s) - 1

cnt = 0
while l < r:
    if s[l] != s[r]:
        if s[l] == "x":
            cnt += 1
            l += 1
        elif s[r] == "x":
            cnt += 1
            r -= 1
        else:
            print(-1)
            exit()
    else:
        l += 1
        r -= 1

print(cnt)