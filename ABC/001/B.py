m = int(input())

if m < 100:
    print("00")
elif m <= 5000:
    m //= 100
    if len(str(m)) == 1:
        print("0"+str(m))
    else:
        print(m)
elif m <= 30000:
    print(m//1000+50)
elif m <= 70000:
    m = (m - 30000) // 5 + 80000
    m //= 1000
    print(m)
else:
    print(89)
