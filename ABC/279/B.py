s = input()
t = input()

flag = False

for i in range(len(s)):
    if len(t)+i <= len(s) and s[i:i+len(t)] == t:
        flag = True
if flag:
    print("Yes")
else:
    print("No")
