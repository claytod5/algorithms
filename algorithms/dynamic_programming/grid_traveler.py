from functools import lru_cache


@lru_cache
def grid_traveler(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 1
    else:
        return grid_traveler(x - 1, y) + grid_traveler(x, y - 1)


if __name__ == "__main__":
    print(grid_traveler(20, 20))
