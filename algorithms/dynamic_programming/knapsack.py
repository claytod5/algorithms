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


if __name__ == "__main__":
    print(number_of_ways(400))
