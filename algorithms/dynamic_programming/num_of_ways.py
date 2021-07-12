from functools import lru_cache


@lru_cache
def number_of_ways(n):
    "Find the number of ways to write n as the sum of 1, 3, 5"
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return number_of_ways(n - 1) + number_of_ways(n - 3) + number_of_ways(n - 5)


def number_of_ways_tab(n):
    table = [0 for i in range(n + 1)]

    table[0] = 1

    for i in range(n + 1):
        if table[i] != 0:
            for j in (1, 3, 5):
                if i + j < len(table):
                    table[i + j] += table[i]

    return table[n]


if __name__ == "__main__":
    print(number_of_ways_tab(109879))
    # print(number_of_ways(9879))
