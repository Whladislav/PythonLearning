def nonrecursive(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def recursive(n):
    if not n:
        return 1
    else:
        return n * recursive(n - 1)


print(recursive(5))
