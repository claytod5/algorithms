from random import randint
from timeit import Timer


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        # pivot = sorted([array[0], array[len(array) // 2], array[-1]])[1] # median of 3
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    a = [randint(0, 1000) for each in range(1000)]
    b = a.copy()

    t2 = Timer("quicksort(b)", "from __main__ import quicksort, b")
    print("quicksort(b): ", t2.timeit(number=1000), "milliseconds")
