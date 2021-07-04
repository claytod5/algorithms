"""Grid Traveler Algorithm.

In how many ways can you travel to the right-bottom square on a grid \
with dimensions x,y."""

memo = {}


def memoize(func, *args):
    def wrapped(x, y):
        if (x, y) not in memo:
            memo[(x, y)] = func(x, y)

        return memo[(x, y)]

    return wrapped


@memoize
def grid_traveler(x, y):
    if x == 0 or y == 0:
        return 0
    elif x == 1 and y == 1:
        return 1
    else:
        return grid_traveler(x - 1, y) + grid_traveler(x, y - 1)


if __name__ == "__main__":
    print(grid_traveler(3, 3))
