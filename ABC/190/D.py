n = int(input())
n2 = n*2
res = 0

def check(i):
    tmp = n2 / i - i + 1
    if tmp % 2 == 0:
        global res
        res += 1

for i in range(1, n2):
    if i * i > n2:
        break
    if n2 % i:
        continue
    y = n2 // i
    check(i)
    if i != y:
        check(y)
    
print(res)