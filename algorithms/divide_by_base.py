"""Divide by Base algorithm for converting from decimal to a different base."""

from data_structures.collections import stack


def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"  # base string

    remstack = stack.Stack()

    while decNumber > 0:
        rem = decNumber % base  # find remainder
        remstack.push(rem)  # add to stack
        decNumber = decNumber // base  # reduce decimal number by base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]  # build new base string

    return newString


if __name__ == "__main__":
    print(baseConverter(15, 16))
