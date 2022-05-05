l, r = map(int, input().split())
l -= 1
r -= 1
s = input()

curr = s[l:r+1]
print(s[:l] + curr[::-1] + s[r+1:])