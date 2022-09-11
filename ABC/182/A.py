a, b = map(int, input().split())

l = 2 * a + 100
print(max(0, l - b))
