def memoize(func, *args):
    memo = {}

    def wrapped(n, a):
        if n not in memo:
            memo[n] = func(n, a)

        return memo[n]

    return wrapped


@memoize
def all_construct(n, a):
    if n == "":
        return [[]]

    result = []

    for each in a:
        if n.startswith(each):
            recur = all_construct(n[len(each) :], a)
            all_ways = [way + [each] for way in recur]
            if all_ways:
                result.extend(all_ways)

    return result


if __name__ == "__main__":
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(all_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(
        all_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        )
    )
