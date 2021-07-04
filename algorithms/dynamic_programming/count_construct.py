def memoize(func, *args):
    memo = {}

    def wrapped(n, a):
        if n not in memo:
            memo[n] = func(n, a)

        return memo[n]

    return wrapped


@memoize
def count_construct(n, a):
    if n == "":
        return 1

    count = 0

    for each in a:
        if n.startswith(each):
            count += count_construct(n[len(each) :], a)

    return count


if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(
        count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    )
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(
        count_construct(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        )
    )
