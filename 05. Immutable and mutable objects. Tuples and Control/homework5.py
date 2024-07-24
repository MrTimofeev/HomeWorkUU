#!/usr/bin/python
#coding: utf-8

immutable_var = (1, "Hello world", [1, 2, 3])
print(immutable_var)

immutable_var[0] = 2
#Примечаение: мы не можем изменить значение кортежа потому что он является неизменяемым 
#Если мы попытаемся запустить код то увидим что он выдает ошибку: 'tuple' object does not support item assignment
#Что в прямом смысле означает: "кортеж" не поддерживает обращение по элементам

immutable_var[2][1] = 2038
print(immutable_var)




