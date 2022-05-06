n = int(input())

if n >= 42:
    n += 1

strN = str(n)
while len(strN) <3:
    strN = "0" + strN
    
print("AGC" + strN)