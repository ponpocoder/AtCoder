s = input()
nums = set()

for i in range(len(s)):
    nums.add(int(s[i]))

for i in range(10):
    if i not in nums:
        print(i)
