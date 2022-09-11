sx, sy, gx, gy = map(int, input().split())

res = ((gy*sx) + (sy*gx)) / (gy+sy)
print(res)
