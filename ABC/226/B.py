n = int(input())
arrays = set()

for _ in range(n):
    array = tuple(map(int, input().split()))[1:]
    arrays.add(array)

print(len(arrays))