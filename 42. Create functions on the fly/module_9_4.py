#!/usr/bin/python
# coding: utf-8

from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: True if x == y else False, first, second)))


def get_advanced_writer(file_name):

    file = open(file_name, mode="w", encoding="utf-8")

    def write_everything(*data_set):
        for data in data_set:
            file.write(str(data) + "\n")
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall():
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
