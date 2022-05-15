x = int(input())

res = float("inf")

for d in range(-9, 10):
    for i in range(1, 10):
        curr = 0
        tmp = i
        while 0 <= tmp < 10:
            curr *= 10
            curr += tmp
            tmp += d
            if x <= curr:
                res = min(res, curr)
                break

print(res)