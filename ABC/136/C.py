n = int(input())
h = list(map(int, input().split()))
i = 0

while i < n - 1:
    if h[i] < h[i+1]:
        h[i+1] -= 1
        i += 1
    elif h[i] == h[i+1]:
        i += 1
    else:
        break

print("Yes" if i == n - 1 else "No")
