def memoize(func, *args):
    memo = {}

    def wrapped(n, a):
        if n not in memo:
            memo[n] = func(n, a)

        return memo[n]

    return wrapped


@memoize
def best_sum(n, a):
    if n == 0:
        return []
    elif n < 0:
        return None

    best = None

    for each in a:
        recur = best_sum(n - each, a)
        if recur is not None:
            new = [each] + recur
            if best is None or len(new) < len(best):
                best = new

    return best


if __name__ == "__main__":
    print(best_sum(7, [5, 7, 4, 3]))
    print(best_sum(100, [1, 2, 5, 25]))
