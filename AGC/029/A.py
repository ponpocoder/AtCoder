s = list(input())

prev = 0
curr = 0
cnt = 0

for i, v in enumerate(s):
    if v == "B":
        prev += i
        cnt += 1

value = len(s) - 1

while cnt:
    curr += value
    cnt -= 1
    value -= 1

print(curr - prev)

