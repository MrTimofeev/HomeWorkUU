#!/usr/bin/python
#coding: utf-8

my_string = input("Введите строку: ")
print("Количество символов в вашей введенной строке:", len(my_string))

print("Строка в верхнем регистре", my_string.upper())
print("Строка в нижнем регистре",my_string.lower())
print("Строка без символов пробела", my_string.replace(" ", ""))
print("Вывод первого символа", list(my_string)[0])
print("Вывод последнего символа", list(my_string)[-1])



