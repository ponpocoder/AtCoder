h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

flag = False
for i in range(1 << h1):
    for j in range(1 << w1):
        array = []
        for k in range(h1):
            if not (i >> k) & 1:
                continue
            curr = []
            for l in range(w1):
                if (j >> l) & 1:
                    curr.append(a[k][l])

            array.append(curr)

        if array == b:
            flag = True
            break

if flag:
    print("Yes")
else:
    print("No")
