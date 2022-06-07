n = int(input())

res = n / 1.08

if int(res) * 108 // 100 == n:
    print(int(res))
elif int(res + 1) * 108 // 100 == n:
    print(int(res + 1))
else:
    print(":(")