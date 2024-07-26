#!/usr/bin/python
#coding: utf-8

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, "test", False]
values_dict = {"a": 234, "b": "Privet", "c": True,}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[1,2], (66, 77)]

print_params(*values_list_2, 42)