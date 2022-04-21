    from itertools import permutations
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))

    x = sorted(permutations(list(range(1, n+ 1))))
    a = x.index(p)
    b = x.index(q)

    print(abs(a - b))
