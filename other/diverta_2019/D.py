n = int(input())
s = set()     
for i in range(1, n):
    if i*i > n:
        break
    if n % i == 0:
        s.add(n%i)
        s.add(n//i)

cnt = 0
for v in s:
    if n // (v-1) == n % (v -1):
        cnt += v - 1

print(cnt)