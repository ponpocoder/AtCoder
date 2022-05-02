n = int(input())

k = 2 ** 31

if -k <= n < k:
    print("Yes")
else:
    print("No")