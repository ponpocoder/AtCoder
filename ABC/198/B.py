n = int(input())

while n % 10 == 0 and n:
    n //= 10

n = str(n)

l, r = 0, len(n)-1

while l < r:
    if n[l] != n[r]:
        print("No")
        exit()
    l += 1
    r -= 1

print("Yes")
