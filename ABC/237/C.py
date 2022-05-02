import sys
s = input()

l, r = 0, len(s) - 1

while l < r:
    if s[l] != s[r]:
        if s[r] == "a":
            r -= 1
        else:
            print("No")
            sys.exit()
    else:
        l += 1
        r -= 1

print("Yes")