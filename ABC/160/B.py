x = int(input())

res = x // 500 * 1000
x %= 500

res += x // 5 * 5
print(res)
