n = int(input())
x = n % 10

if x in [2, 4, 5, 7, 9]:
    print("hon")
elif x in [0, 1, 6, 8]:
    print("pon")
else:
    print("bon")
