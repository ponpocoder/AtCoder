n = int(input())
cnt = [0] * 4

for _ in range(n):
    s = input()
    if s == "AC":
        cnt[0] += 1
    elif s == "WA":
        cnt[1] += 1
    elif s == "TLE":
        cnt[2] += 1
    else:
        cnt[3] += 1

print("AC x", cnt[0])
print("WA x",  cnt[1])
print("TLE x", cnt[2])
print("RE x", cnt[3])
