import bisect
from array import array

l, q = map(int, input().split())

curr = array("i", [0, l])
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(curr, x)
    else:
        idx = bisect.bisect_right(curr, x)
        print(curr[idx] - curr[idx - 1])