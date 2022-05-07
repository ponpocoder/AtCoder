s = input()
k = int(input())

l = 0
r = 0
curr = 0
res = 0

while r < len(s):
    if s[r] == "X":
        curr += 1
        r += 1
    elif k > 0:
        curr += 1
        r += 1
        k -= 1
    else:
        res = max(res, curr)
        if s[l] == ".":
            k += 1
        l += 1
        curr -= 1
res = max(res, curr)
print(res)

# n = len(s)

# cnt = 0
# r = - 1
# res = 0

# for l in range(n):
#     while r < n:
#         if r == n - 1 or (s[r+1] == "." and cnt == k):
#             break
#         if s[r+1] == ".":
#             cnt += 1
#         r += 1
#     res = max(res, r - l + 1)
#     if s[l] == ".":
#         cnt -= 1

# print(res)