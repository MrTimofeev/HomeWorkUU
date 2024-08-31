#!/usr/bin/python
# coding: utf-8

from threading import Thread
from time import sleep


class Knight(Thread):

    #Сам вопрос: Как это работает?
    # Если вызывать инит после объявление атрибутов выбивает ошибку: AssertionError: Thread.__init__() not called
    # Хотя инит вызывается, для примера: 
    # Ссылка на видео урок: https://urban-university.ru/members/courses/course999421818026/20231210-0000potoki-na-klassah-829597843726
    # Название видео урока: 2023/12/10 00:00|Потоки на классах
    # Вызов с такой последовательностью: объявление атрибута а затем инит не выбивает ошибку в видео но выбивает у меня  | тайм код видео урока 8:10
    # def __init__(self, name, power):
    #     self.name = name
    #     super().__init__()
        
    # У меня почему-то не выбивает ошибку только если сначал вызывать инит, а после объявлять атрибуты
    def __init__(self, name, power):
        super().__init__()
        self.name = name

    # Есть предположение что это из-за используемого ide, но это не точено так как фактически
    # используется один и тот же интерпритатор 

    def run(self):
        print(f"{self.name}, на нас напали!")
        
            


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
