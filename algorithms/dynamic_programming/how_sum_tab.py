def how_sum_tab(n, a):
    table = [None for i in range(n + 1)]
    table[0] = []

    for i in range(n + 1):
        if table[i] is not None:
            for j in a:
                if (i + j) < len(table):
                    table[i + j] = table[i] + [j]

    return table[n]


if __name__ == "__main__":
    print(how_sum_tab(7, [5, 3, 4, 7]))
    print(how_sum_tab(7, [2, 3]))
    print(how_sum_tab(7, [2, 4]))
    print(how_sum_tab(8, [2, 3, 5]))
    print(how_sum_tab(300, [7, 14]))
