#!/usr/bin/python
# coding: utf-8

class calculate():
    def add_everything_up(self, a, b):
        try:
            return round(a + b, 3)
        except TypeError as ex:
            return str(a) + str(b)

Calculator = calculate()

print(Calculator.add_everything_up(123.456, 'строка'))
print(Calculator.add_everything_up('яблоко', 4215))
print(Calculator.add_everything_up(123.456, 7))