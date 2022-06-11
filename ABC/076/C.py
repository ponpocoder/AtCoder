s = input()
t = input()
res = []

for i in range(len(s) - len(t), -1, -1):
    isSame = True
    for j in range(len(t)):
        if s[i+j] != "?" and s[i+j] != t[j]:
            isSame = False
            break
    
    if isSame:
        for j in range(i):
            if s[j] == "?":
                res.append("a")
            else:
                res.append(s[j])
        for j in range(len(t)):
            res.append(t[j])
        for j in range(i+len(t), len(s)):
            if s[j] == "?":
                res.append("a")
            else:
                res.append(s[j])
        print("".join(res))
        exit()
        
print("UNRESTORABLE")