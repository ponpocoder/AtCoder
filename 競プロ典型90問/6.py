n, k = map(int, input().split())
s = input()

chars = [""] * n
for i, c in enumerate(s):
    chars[i] = c
chars.sort()
ans = ""
for i in range(k):
    ans += chars[i]
print(ans)