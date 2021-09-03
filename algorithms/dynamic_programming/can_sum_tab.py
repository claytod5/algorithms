def can_sum_tab(n, a):
    table = [False for each in range(n + 1)]
    table[0] = True

    for i in range(n + 1):
        if table[i] is True:
            for j in a:
                if i + j < len(table):
                    table[i + j] = True

    return table[n]


if __name__ == "__main__":
    print(can_sum_tab(7, [5, 3, 4]))
    print(can_sum_tab(7, [2, 4]))
    print(can_sum_tab(300, [7, 14]))
