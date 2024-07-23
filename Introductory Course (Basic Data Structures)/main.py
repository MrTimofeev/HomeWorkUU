#!/usr/bin/python
#coding: utf-8

# 1st programm
result1 = (9**0.5)*5
print("Result 1 task:", result1)

# 2st programm
result2 = 9.99 > 9.98 and 1000 != 1000.1
print("Result 2 task:", result2)

# 3st programm
number1 = 1234 // 10 % 100
number2 = 5678 // 10 % 100
result3 = number1 + number2
print("Result 3 task:", result3)

# 4st programm
intnum1 = int(13.42)
intnum2 = int(42.13)
floatnum1 = int(13.42%13*100)
floatnum2 = int(42.13%42*100)
result4 = intnum1 == intnum2 or intnum1 == floatnum2 or intnum2 == floatnum1 
print("Result 4 task:", result4)

# Описание решения 4 задачи:
# 1) Отделяем целое у двух заданных чисел
# 2) Отделяем числа после запятой для сравнение приводим их к целочисленному значению
# 3) Сравниваем и выводим результат
# Примечание при отделение числа после запятой а именно floatnum1 в результате мы получаем 41 а не 42
# Это связанно с ограничем точности представления чисел с плавающей запятой то есть:
# при отделении числа после запятой 13.42%13 итогом будет 0.41999999999999993 как раз таки из-за ограничение точности 
# поэтому в результате перевода в целоцисленное мы получаем 41 а не 42  





