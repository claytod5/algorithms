def can_construct_tab(n, a):
    table = [False for i in range(len(n) + 1)]
    table[0] = True

    #     breakpoint()
    for i in range(len(n) + 1):
        if table[i] is True:
            for j in a:
                if j == n[i : i + len(j)]:
                    table[i + (len(j))] = True

    return table[len(n)]


if __name__ == "__main__":
    print(can_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(
        can_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    )
    print(
        can_construct_tab(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        )
    )
