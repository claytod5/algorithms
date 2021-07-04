def memoize(func, *args):
    memo = {}

    def wrapped(n, a):
        if n not in memo:
            memo[n] = func(n, a)

        return memo[n]

    return wrapped


@memoize
def how_sum(n, a):
    if n == 0:
        return []
    elif n < 0:
        return None

    for each in a:
        recur = how_sum(n - each, a)
        if recur is not None:
            return [each] + recur

    return None


if __name__ == "__main__":
    print(how_sum(7, [7, 5, 2, 8, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(7, [2, 4]))
    print(how_sum(0, [1, 2, 3]))
    print(how_sum(300, [7, 14]))
