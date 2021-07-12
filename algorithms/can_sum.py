from functools import lru_cache


def can_sum(n, a):
    if n == 0:
        return True
    elif n < 0:
        return False

    for each in a:
        if can_sum(n - each, a) is True:
            return True

    return False


if __name__ == "__main__":
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(300, [7, 14]))
