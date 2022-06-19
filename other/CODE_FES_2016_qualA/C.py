s = list(input())
k = int(input())

for i in range(len(s)):
    d = ord("z") - ord(s[i]) + 1
    if d <= k and s[i] != "a":
        k -= d
        s[i] = "a"

if k:
    s[-1] = chr(ord(s[-1]) + k % 26)

print("".join(s))