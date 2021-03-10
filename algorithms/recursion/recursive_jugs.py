"""
Write a program to solve the following problem: You have two jugs: a 4-gallon
jug and a 3-gallon jug. Neither of the jugs have markings on them. There is a
pump that can be used to fill the jugs with water. How can you get exactly two
gallons of water in the 4-gallon jug?
"""


def recursive_jugs(big_jug, little_jug, amt):
    """Displays how to get amt when given a big jug and little jug without
    markings

    :big_jug: TODO
    :little_jug: TODO
    :amt: TODO
    :returns: TODO

    """

    if little_jug == amt:
        print(f"Little jug:{little_jug} equals target:{amt}")

        return "Dump big jug and fill with remainder in little jug"
    else:
        print("Dump big jug")
        print("Fill big jug with little jug")
        big = little_jug
        print(f"Big jug:{big}")
        print("Refill little jug and put into big jug")
        little = little_jug - (big_jug % little_jug)
        # big = big_jug
        print(f"Little jug:{little}")

        return recursive_jugs(big, little, amt)


if __name__ == "__main__":
    print(recursive_jugs(4, 3, 2))
