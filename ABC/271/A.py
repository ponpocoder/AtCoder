n = int(input())
dic = "0123456789ABCDEF"

x = n // 16
y = n % 16

res = dic[x] + dic[y]

print(res)
