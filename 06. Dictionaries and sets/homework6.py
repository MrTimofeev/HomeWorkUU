#!/usr/bin/python
#coding: utf-8

#Работа с словарем
my_dict = {
    "Denis": 2000,
    "Anton": 1998,
    "Mark": 2001,
    "Eva": 2004,
    }

print("Вывод словаря:" , my_dict)
print("Вывод словаря по существующему ключу (Eva):" ,my_dict["Eva"])
print("Вывод словаря по не существующему ключу:" , my_dict.get("Sasha"))

my_dict.update({
    "Sonya": 1999,
    "Stas": 1997 
})
print("Добавили 2 пары в словарь:", my_dict)


item = my_dict.pop("Eva")
print("Вывод значения удаленной пары", item)
print("Словарь после удаления ключа:", my_dict)

print("-----------------------------------------")

#Работа с множеством
my_set = { 1, 1, 2, 2, 3, 3, "test", "test"}
print("Вывод множества: ", my_set)

my_set.update((5, 7))
print("Вывод обновленного множества", my_set)

my_set.discard(2)
print("Вывод множества после удаления", my_set)








