def factorial(n):
    res = 1

    for i in range(1, n):
        res *= i + 1

    return res


def factorial_recursive(n):
    if n < 2:
        return n
    else:
        return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    print(factorial(30))
    print(factorial_recursive(30))
