n = int(input())
divisors = []

for i in range(1, n+1):
    if i*i > n:
        break
    if n % i == 0:
        divisors.append(n//i)
        divisors.append(i)


divisors.sort()

cnt = 0
for v in divisors:
    if v == 1:
        continue
    curr = v
    while n % curr == 0:
        n //= curr
        curr *= v
        cnt += 1

print(cnt)