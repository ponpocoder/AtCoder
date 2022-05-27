a, b, w = map(int, input().split())
w *= 1000
mn, mx = 0, 0
cnt = 0
resMin = 0
resMax = 0

while True:
    mn += a
    mx += b
    cnt += 1
    if mn <= w <= mx:
        if resMax == 0:
            resMax = cnt
        resMin = cnt
    elif w < mn:
        if resMax == 0:
            print("UNSATISFIABLE")
            exit()
        else:
            break

print(resMax, resMin)

