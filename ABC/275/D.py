from collections import defaultdict

n = int(input())
dic = defaultdict(int)
def f(i):
    if i == 0:
        return 1
    if i in dic:
        return dic[i]
    dic[i] = f(i//2)+f(i//3)
    return dic[i]

print(f(n))
