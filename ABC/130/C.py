w, h, x, y = map(int, input().split())

cx = w / 2
cy = h / 2
area = w * h / 2

if cx == x and cy == y:
    print(area, 1)
else:
    print(area, 0)