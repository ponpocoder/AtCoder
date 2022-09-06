a, b, c = map(int, input().split())

if c == 0:
    print("Takahashi" if a > b else "Aoki")
else:
    print("Aoki" if b > a else "Takahashi")
