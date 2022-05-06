import sys
s = input()
t = "oxxoxxoxxoxx"

for i in range(3):
    if t[i:i+len(s)] == s:
        print("Yes")
        sys.exit()
        
print("No")