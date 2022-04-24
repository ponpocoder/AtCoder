from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
dic = defaultdict(int)
for value in a:
    dic[value] += 1

def getDivisors(num):
    divs = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:        
            divs.append(i)
            divs.append(num // i)
        if divs[-1] == divs[-2]:
            divs.pop()
    
    return divs


res = 0
for va, ta in dic.items():
    divs = getDivisors(va)

    for vb in divs:
        vc = va // vb

        tb = dic[vb] if vb in dic else 0
        tc = dic[vc] if vc in dic else 0
        
        res += ta * tb * tc

print(res)