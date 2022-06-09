from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

dic = defaultdict(int)

for v in a:
    dic[v] += 1

keys = list(dic.keys())

if len(keys) == 1 and keys[0] == 0:
    print("Yes")
elif len(keys) == 2 and ((dic[keys[0]] == 2*n // 3 and dic[keys[1]] == n // 3) or (dic[keys[1]] == 2*n // 3 and dic[keys[0]] == n // 3)):
    print("Yes")
elif len(keys) == 3 and dic[keys[0]] == dic[keys[1]] == dic[keys[2]] == n // 3 and keys[0] ^ keys[1] ^ keys[2] == 0:
    print("Yes")
else:
    print("No")