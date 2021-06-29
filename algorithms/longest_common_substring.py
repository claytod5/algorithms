#!/usr/bin/env python


def longest_common_substring(a, b):
    """Return the longest common substring between a and b.

    Args:
        a (str): A word or non-word string.
        b (str): A word or non-word string.

    Returns:
        res (str): The longest common substring found between a and b.

    """
    memo = {}
    if a and b:
        for i in range(len(a)):
            if a[i] == b[i]:
                if i == 0 or memo[i - 1] == 0:
                    memo[i] = a[i]
                else:
                    memo[i] = memo[i - 1] + a[i]
            else:
                memo[i] = 0
        return memo[max(memo)]


if __name__ == "__main__":
    print(longest_common_substring("bus", "gus"))
