#!/usr/bin/python
# coding: utf-8

def calculate_structure_sum(*data_structure, **dict_):
    result = 0
    # print(data_structure)
    for item in data_structure:
        if isinstance(item, str):
            result = result + len(item)
        elif isinstance(item, dict):
            result = result + calculate_structure_sum(**item)
        elif isinstance(item, list):
            result = result + calculate_structure_sum(*item)
        elif isinstance(item, set):
            result = result + calculate_structure_sum(*item)
        elif isinstance(item, tuple):
            result = result + calculate_structure_sum(*item)
        else:
            result = result + item

    if isinstance(dict_, dict):
        for key, value in dict_.items():
            if isinstance(key, str):
                result = result + len(key)
            elif isinstance(key, int):
                result = result + key
            elif isinstance(key, dict):
                result = result + calculate_structure_sum(*key)

            if isinstance(value, str):
                result = result + len(value)
            elif isinstance(value, int):
                result = result + value
            elif isinstance(value, list):
                result = result + calculate_structure_sum(*value)
            elif isinstance(value, dict):
                result = result + calculate_structure_sum(**value)
            elif isinstance(value, tuple):
                result = result + calculate_structure_sum(*value)
            elif isinstance(value, set):
                result = result + calculate_structure_sum(*value)

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
