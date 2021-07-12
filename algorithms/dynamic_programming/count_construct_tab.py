def count_construct_tab(n, a):
    table = [0 for i in range(len(n) + 1)]
    table[0] = 1

    for i in range(len(n) + 1):
        if table[i] >= 1:
            for j in a:
                if j == n[i : i + len(j)]:
                    table[i + len(j)] += table[i]

    return table[len(n)]


if __name__ == "__main__":
    print(count_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(
        count_construct_tab(
            "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]
        )
    )
    print(
        count_construct_tab(
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        )
    )
