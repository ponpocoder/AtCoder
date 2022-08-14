r, c = map(int, input().split())
if r >= 9:
    r = 16 - r
black = True
if r == 2 and 2 <= c <= 14:
    black = False
if r == 3 and (c == 2 or c == 14):
    black = False
if r == 4 and (c == 2 or c == 14 or 4 <= c <= 12):
    black = False
if r == 5 and (c == 2 or c == 4 or c == 12 or c == 14):
    black = False
if r == 6 and (c == 2 or c == 4 or c == 12 or c == 14 or 6 <= c <= 10):
    black = False
if r == 7 and (c == 2 or c == 4 or c == 6 or c == 10 or c == 12 or c == 14):
    black = False
if r == 8 and (c == 2 or c == 4 or c == 6 or c == 8 or c == 10 or c == 12 or c == 14):
    black = False

if black:
    print("black")
else:
    print("white")
