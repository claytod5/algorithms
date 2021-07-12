def all_construct_tab(n, a):
    table = [[] for i in range(len(n) + 1)]
    table[0] = [[]]

    for i in range(len(n) + 1):
        if len(table[i]) > 0:
            for j in a:
                if j == n[i : i + len(j)]:
                    table[i + len(j)] += [way + [j] for way in table[i]]

    return table[len(n)]


if __name__ == "__main__":
    print(all_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(all_construct_tab("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(
        all_construct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    )
