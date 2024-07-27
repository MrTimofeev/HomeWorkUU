#!/usr/bin/python
# coding: utf-8


def sumutor_list(list_):
    sum_list = 0
    for item in list_:
        if isinstance(item, str) or not item:
            sum_list = sum_list + len(item)
        elif isinstance(item, dict):
            sum_list = sum_list + sumator_dict(item)
        elif isinstance(item, tuple):
            sum_list = sum_list + sumator_tuple(item)
        elif isinstance(item, set):
            sum_list = sum_list + sumator_set(item)
        elif isinstance(item, list):
            sum_list = sum_list + sumutor_list(item)
        else:
            sum_list = sum_list + item
    return sum_list


def sumator_dict(dict_):
    sum_dict = 0
    for key, value in dict_.items():
        if isinstance(value, str) or not value:
            sum_dict = sum_dict + len(value)
        elif isinstance(value, list):
            sum_dict = sum_dict + sumutor_list(value)
        elif isinstance(value, tuple) > 0:
            sum_dict = sum_dict + sumator_tuple(value)
        elif isinstance(value, set):
            sum_dict = sum_dict + sumator_set(value)
        elif isinstance(value, dict):
            sum_dict = sum_dict + sumator_dict(value)
        else:
            sum_dict = sum_dict + value + len(key)
    return sum_dict


def sumator_tuple(tuple_):
    sum_tuple = 0
    for item in tuple_:
        if isinstance(item, str) or not item:
            sum_tuple = sum_tuple + len(item)
        elif isinstance(item, list):
            sum_tuple = sum_tuple + sumutor_list(item)
        elif isinstance(item, dict):
            sum_tuple = sum_tuple + sumator_dict(item)
        elif isinstance(item, set):
            sum_tuple = sum_tuple + sumator_set(item)
        elif isinstance(item, tuple):
            sum_tuple = sum_tuple + sumator_tuple(item)
        else:
            sum_tuple = sum_tuple + item
    return sum_tuple


def sumator_set(set_):
    sum_set = 0
    for item in set_:
        if isinstance(item, str) or not item:
            sum_set = sum_set + len(item)
        elif isinstance(item, list):
            sum_set = sum_set + sumutor_list(item)
        elif isinstance(item, dict):
            sum_set = sum_set + sumator_dict(item)
        elif isinstance(item, tuple):
            sum_set = sum_set + sumator_tuple(item)
        elif isinstance(item, set):
            sum_set = sum_set + sumator_set(item)
        else:
            sum_set = sum_set + item
    return sum_set


def calculate_structure_sum(data_structure):
    result = 0
    for item in data_structure:
        if isinstance(item, str):
            result = result + len(item)
        elif isinstance(item, list):
            result = result + sumutor_list(item)
        elif isinstance(item, dict):
            result = result + sumator_dict(item)
        elif isinstance(item, tuple):
            result = result + sumator_tuple(item)
        elif isinstance(item, set):
            result = result + sumator_set(item)
        else:
            result = result + item
    return result 


# Исходные данные
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)
print(result)