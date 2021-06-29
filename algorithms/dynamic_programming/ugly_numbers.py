def ugly_num(n):
    if n <= 6:
        return n
    else:
        return ugly_num(n - 2) % ugly_num(n - 4)


if __name__ == "__main__":
    print(ugly_num(7))
