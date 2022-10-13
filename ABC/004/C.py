n = int(input())
n %= 30

x = ["1", "2", "3", "4", "5", "6"]

for i in range(n):
    x[i % 5], x[i % 5 + 1] = x[i % 5 + 1], x[i % 5]

print("".join(x))
