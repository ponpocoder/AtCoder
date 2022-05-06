from collections import defaultdict

n = int(input())
dic = defaultdict(int) 
for _ in range(n):
    s = input()
    dic[s] += 1

res = ""
cnt = 0
for key, value in dic.items():
    if value > cnt:
        cnt = value
        res = key

print(res)