#!/usr/bin/python
# coding: utf-8


def apply_all_func(int_list, *functions):
    result_dict = {}

    for func in functions:
        result_dict[func.__name__] = func(int_list)

    return result_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
