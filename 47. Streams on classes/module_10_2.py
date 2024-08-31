#!/usr/bin/python
# coding: utf-8

from threading import Thread
from time import sleep


class Knight(Thread):
    
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        
        

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_day = 1
        
        while True:
            self.enemy = self.enemy - self.power
            print(f"{self.name} сражается {count_day} день(дня)..., осталось {self.enemy} воинов.")
            if self.enemy <= 0:
                print(f"{self.name} одержал победу спустя {count_day} дней(дня)!")
                break
            count_day += 1
            
            sleep(1)
           
            


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()