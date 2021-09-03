def best_sum(n, a, best=[]):
    if n == 0:
        return []
    elif n < 0:
        return None

    for each in a:
        recur = best_sum(n - each, a, best)
        if recur is not None:
            new = [each] + recur
            if not best:
                best = new
            elif len(best) > len(new):
                best = new


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))
