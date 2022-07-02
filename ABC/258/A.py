k = int(input())
hour = 21

hour += k // 60
minute = str(k % 60)
if len(minute) == 1:
    minute = "0" + minute

res = str(hour)+":"+str(minute)
print(res)
