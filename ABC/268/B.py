s = input()
t = input()

if len(s) > len(t):
    print("No")
else:
    if t[:len(s)] == s:
        print("Yes")
    else:
        print("No")
