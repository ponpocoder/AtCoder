import sys

s = input()
t = input()

diff = (ord(t[0]) - ord(s[0])) % 26

for i in range(1, len(s)):
    curr = (ord(t[i]) - ord(s[i])) % 26
    if curr != diff:
        print("No")
        sys.exit()

print("Yes")