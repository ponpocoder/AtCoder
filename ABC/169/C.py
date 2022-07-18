a, b = input().split()

a = int(a)
bf, bb = b.split('.')
b = int(bf)*100+int(bb)

print(a*b//100)