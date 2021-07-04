def memoize(func, *args):
    memo = {}

    def wrapped(n, a):
        if n not in memo:
            memo[n] = func(n, a)

        return memo[n]

    return wrapped


@memoize
def can_construct(n, a):
    if n == "":
        return True

    for each in a:
        # don't take out from middle because it would create
        # a string of characters that do not necessarily appear in the original
        # string. It is better to take out from prefix because you preserve
        # the adjacent strings in the original. Also, the candidate strings
        # have to match the prefix or suffix if they are able to construct the
        # original string
        if n.startswith(each):
            if can_construct(n[len(each) :], a) is True:
                return True

    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(
        can_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        )
    )
