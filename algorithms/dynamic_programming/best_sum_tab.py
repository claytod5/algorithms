def best_sum_tab(n, a):
    table = [None for i in range(n + 1)]
    table[0] = []

    for i in range(n + 1):
        if table[i] is not None:
            for j in a:
                if (i + j) < len(table):
                    temp = table[i] + [j]
                    if table[i + j] is None:
                        table[i + j] = temp
                    elif len(temp) < len(table[i + j]):
                        table[i + j] = temp

    return table[n]


if __name__ == "__main__":
    print(best_sum_tab(7, [5, 3, 4, 7]))
    print(best_sum_tab(8, [2, 3, 5]))
    print(best_sum_tab(8, [1, 4, 5]))
    print(best_sum_tab(100, [1, 2, 5, 25]))
