#!/usr/bin/python
# coding: utf-8


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (len(i[0]) - len(i[1]) for i in list(zip(first, second)) if len(i[0]) != len(i[1]))
print(list(first_result))

second_result = (True if len(first[x]) == len(second[x]) else False for x in range(len(first)))
print(list(second_result))
