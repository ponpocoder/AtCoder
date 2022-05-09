n, q = map(int, input().split())

X = [int(input()) for _ in range(q)]
array = [i+1 for i in range(n)]
pos = [i for i in range(n)]

def swap(i, j):
    array[i], array[j] = array[j], array[i]

for x in X:
    currPos = pos[x-1]
    if currPos == n - 1:
        nxtN = array[currPos - 1]
        swap(currPos, currPos - 1)
        pos[x-1] = currPos - 1
        pos[nxtN-1] = currPos
    else:
        nxtN = array[currPos + 1]
        swap(currPos, currPos+1)
        pos[x-1] = currPos + 1
        pos[nxtN-1] = currPos

print(*array)

