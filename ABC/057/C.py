n = int(input())
res = float("inf")
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        a = str(i)
        b = str(n // i)
        res = min(res, max(len(a),len(b)))
print(res)
