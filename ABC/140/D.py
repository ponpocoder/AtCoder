n, k = map(int, input().split())
s = input()
score = 0

for i in range(1, n):
    if s[i] == s[i-1]:
        score += 1

res = min(score + 2 * k, n -1)
print(res)