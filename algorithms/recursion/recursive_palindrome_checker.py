def recursive_palindrome_checker(palindrome):
    first = palindrome[0]
    last = palindrome[-1]

    if len(palindrome) <= 3:
        if first == last:
            return True
        else:
            return False

    if first == last:
        return recursive_palindrome_checker(palindrome[1 : len(palindrome) - 1])
    else:
        return False


if __name__ == "__main__":
    print(recursive_palindrome_checker("wassamassaw"))
