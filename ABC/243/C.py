import sys
n = int(input())
x = []
y = []
for i in range(n):
    pair = list(map(int,(input().split())))
    x.append(pair[0])
    y.append(pair[1])
s = input()

dict = {}

for i in range(n):
    if y[i] in dict:
        dict[y[i]].append(i)         
    else:
        dict[y[i]] = [i]

for y in dict:
    currMin = float("-inf")
    currMax = float("inf")
    for i in dict[y]:
        if (x[i] < currMin and s[i] == "R") or (x[i] > currMax and s[i] == "L"):
            print("Yes")
            sys.exit()
        else:
            if s[i] == "R":
                currMax = min(currMax,x[i])
            else:
                currMin = max(currMin,x[i])
print("No")