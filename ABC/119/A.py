s = input()

y = int(s[:4])
m = int(s[5:7])
d = int(s[8:])

flag = True

if y < 2019 or (y == 2019 and m < 4) or (y == 2019 and m == 4 and d <= 30):
    print("Heisei")
else:
    print("TBD")
