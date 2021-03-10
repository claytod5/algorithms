#! /usr/bin/env python3

from timeit import Timer

test_list = [x for x in range(100000)]


def list_linear():
    for each in test_list:
        if each == 10400:
            return 10400


askii = [chr(x) for x in range(63, 130)]

# test_dict = {askii[x]): ord(x) for x in askii}
test_dict = dict()

for each in askii:
    test_dict.update({each: ord(each)})


def dict_linear_get(d, key):
    for k, v in d.items():
        if k == key:
            return {k: v}


def dict_linear_set(d, key, value):
    for k, v in d.items():
        if k == key:
            d[key] = value


if __name__ == "__main__":
    print("-----------List tests----------")

    t1 = Timer("test_list.index(400)", "from __main__ import test_list")
    print("Index Test: ", t1.timeit(number=1000), "milliseconds", end="\n")

    t2 = Timer("list_linear()", "from __main__ import list_linear")
    print("List Linear Test: ", t2.timeit(number=1000), "milliseconds")

    print("-------------------------------", end="\n\n")

    print("-----------Dict tests----------")

    t3 = Timer("test_dict.get('h')", "from __main__ import test_dict")
    print("Dict Get Test: ", t3.timeit(number=1000), "milliseconds", end="\n")

    t4 = Timer(
        "dict_linear_get(test_dict, 'h')",
        "from __main__ import \
               test_dict, dict_linear_get",
    )
    print("Dict Linear Get Test: ", t4.timeit(number=1000), "milliseconds", end="\n\n")

    t5 = Timer("test_dict['h'] = 1300", "from __main__ import test_dict")
    print("Dict Set Test: ", t5.timeit(number=1000), "milliseconds", end="\n")

    t6 = Timer(
        "dict_linear_set(test_dict, 'h', 1300)",
        "from __main__ import \
               test_dict, dict_linear_set",
    )
    print("Dict Set Test: ", t6.timeit(number=1000), "milliseconds", end="\n")

    print("-------------------------------")
