x = input()

s = 0
for c in x:
    s += int(c)

res = []
curr = 0
carry = 0
for i in reversed(range(len(x))):
    curr = s + carry
    res.append(curr % 10)
    carry = curr // 10
    s -= int(x[i])

while carry > 0:
    res.append(carry % 10)
    carry //= 10

res.reverse()
print("".join(str(x) for x in res))