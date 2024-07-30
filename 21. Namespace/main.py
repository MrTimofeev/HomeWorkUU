#!/usr/bin/python
# coding: utf-8


def test_function():
    print("Функция test_function")
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return

inner_function()

"""результатом работы данного кода будет ошибка потому, что 
мы не можем обратиться к функции находящейся внутри функции т.к она находится
за пределами области видимости, но при этом мы можем сделать наоборт обращаться из
функции inner_function к глобальному пространству имен
"""