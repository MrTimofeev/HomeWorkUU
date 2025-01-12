#!/usr/bin/python
#coding: utf-8

# 1st program
print((9 ** 0.5) * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
result1 = 2 * 2 + 2  # Без приоритета (умножение выполняется первым)
result2 = 2 * (2 + 2)  # С приоритетом для сложения
print(result1)
print(result2)
print(result1 == result2)

# 4th program
number = float('123.456')  # Преобразуем строку в дробное число
number *= 10  # Умножаем на 10, чтобы сместить первую цифру после точки в целую часть
first_digit_after_decimal = int(number) % 10  # Получаем первую цифру после точки
print(first_digit_after_decimal)