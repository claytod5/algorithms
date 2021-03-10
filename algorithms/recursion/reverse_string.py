def reverse_str(string):
    """
    Base case: length of string
    Modification: str slice
    """

    if len(string) == 1:
        return string

    return reverse_str(string[1:]) + string[0]


if __name__ == "__main__":
    print(reverse_str("december"))
    print("december"[::-1])
