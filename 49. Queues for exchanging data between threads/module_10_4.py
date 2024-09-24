#!/usr/bin/python
# coding: utf-8

from threading import Thread
import queue
from random import randint
from time import sleep


class Table():
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe():
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        flag = True
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    table.guest = guest
                    guest.start()
                    flag = True
                    break
                else:
                    flag = False

            if flag == False:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)

    def discuss_guests(self):
        while True:
            if not self.queue.empty():
                for table in self.tables:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest = None
                        print(f"Стол номер {table.number} свободен")

                    if table.guest == None:
                        table.guest = self.queue.get()
                        print(
                            f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()
            else:
                break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
