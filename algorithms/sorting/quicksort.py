def quicksort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        left = [i for i in a[1:] if i <= pivot]
        right = [i for i in a[1:] if i > pivot]

        return quicksort(left) + [pivot] + quicksort(right)
