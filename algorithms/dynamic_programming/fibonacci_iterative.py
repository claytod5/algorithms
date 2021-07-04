def fib_iter(n):
    prev_two = 0
    prev_one = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for each in range(n - 1):
            res = prev_two + prev_one
            prev_two, prev_one = prev_one, res
        return res
