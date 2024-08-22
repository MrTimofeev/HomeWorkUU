#!/usr/bin/python
# coding: utf-8

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, "r+", encoding="utf-8")
        result_data = file.read()
        file.close()
        return result_data

    def add(self, *products):
        text_in_file = self.get_products().split("\n")
        file = open(self.__file_name, "w", encoding="utf-8")
        for item in products:
            if str(item) in text_in_file:
                print(f"Продукт {str(item)} уже есть в магазине")
            else:
                text_in_file.append(f"{str(item)}")
        file.write("\n".join(text_in_file).strip())
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
