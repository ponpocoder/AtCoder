n = int(input())
a = list(map(int, input().split()))

s = set(a)

print("YES" if len(s) == n else "NO")
