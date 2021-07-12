def memoize(func, *args):
    memo = {}

    def wrapped(*args):
        if (args) not in memo:
            memo[args] = func(*args)

        return memo[args]

    return wrapped


@memoize
def longest_common_subsequence(a, b, i, j):
    if i == 0 or j == 0:
        return 0
    elif a[i - 1] == b[j - 1]:
        return 1 + longest_common_subsequence(a, b, i - 1, j - 1)
    else:
        return max(
            longest_common_subsequence(a, b, i - 1, j),
            longest_common_subsequence(a, b, i, j - 1),
        )


def lcs_tab(a, b):
    table = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] += table[i - 1][j - 1] + 1
            else:
                # fills table cells with current maximum lcs
                table[i][j] += max(table[i - 1][j], table[i][j - 1])

    return table[len(b)][len(a)]


if __name__ == "__main__":
    print(longest_common_subsequence("ABCDGH", "AEDFHR", 6, 6))
    print(lcs_tab("ABCDGH", "AEDFHR"))
