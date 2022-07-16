n = int(input())

def f(n):
    return (n+1)*n//2

res = 0
for i in range(1, n+1):
    res += i * f(n//i)

print(res)

# エラストテネス O(NlogN)
# n = int(input())
# cnt = [1] * (n+1)
# cnt[0] = 0

# for i in range(2, n+1):
#     for j in range(i, n+1, i):
#         cnt[j] += 1

# res = 0
# for i in range(n+1):
#     res += i * cnt[i]

# # print(cnt)
# print(res)