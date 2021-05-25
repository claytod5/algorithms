from random import randint
from timeit import Timer

# pivot = sorted([a[0], a[len(a) // 2], a[-1]])[1] # median of 3


def quicksort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        left = [i for i in a[1:] if i <= pivot]
        right = [i for i in a[1:] if i > pivot]

        return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    a = [randint(0, 1000) for each in range(1000)]
    b = a.copy()

    t2 = Timer("quicksort(b)", "from __main__ import quicksort, b")
    print("quicksort(b): ", t2.timeit(number=1000), "milliseconds")
