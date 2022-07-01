s = int(input())

a = (s + 10**9 - 1) // 10**9
b = 10**9 * a - s

print(0, 0, 10**9, 1, b, a)