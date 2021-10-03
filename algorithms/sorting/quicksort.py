def pysort(a):
    """Concise implementation of QuickSort, however it violates the space complexity
    since this version appends to new lists during the partitioning. QuickSort should
    do in-place paritioning."""
    if len(a) < 2:
        return a
    else:
        pivot, *rest = a
        left, right = [], []
        for each in rest:
            (left if each <= pivot else right).append(each)

        return pysort(left) + [pivot] + pysort(right)


def lomuto_partition(a, low, high):
    i = low - 1  # set i as less than lowest index
    pivot = a[high]  # set pivot as last item's value

    for j in range(low, high):

        # If current element is smaller than or equal to pivot

        # If not, then j will increase, but i will not, pointing to a larger item
        # i will get 'stuck' on an item larger than pivot
        # That pointer is then used to swap with another item that is smaller than pivot
        if a[j] <= pivot:

            i += 1
            a[i], a[j] = a[j], a[i]  # swap

    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def hoare_partition(a, low, high):
    """Makes 3 times fewer swaps on average than lomuto's partition scheme."""
    pivot = a[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]


def quicksort(a, low, high):
    """Proper implementation of quicksort in Python, complying with the time and space
    complexities of quicksort.

    At least twice as fast as pysort when using hoare partitioning.
    """
    if len(a) == 1:
        return a
    if low < high:

        partition_idx = hoare_partition(a, low, high)

        quicksort(a, low, partition_idx)
        quicksort(a, partition_idx + 1, high)


if __name__ == "__main__":
    a = [8, 123, 67, 1, 3, 2, 9, 1083, 313]
    quicksort(a, 0, len(a) - 1)
    print(a)
