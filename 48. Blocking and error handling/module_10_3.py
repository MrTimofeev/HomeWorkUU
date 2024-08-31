#!/usr/bin/python
# coding: utf-8

from threading import Thread, Lock
from random import randint
from time import sleep

class Bank():

    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):

        for i in range(1, 101):
            rand_num = randint(50, 500) 
            self.balance += rand_num
            print(F"Пополнение: {rand_num}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            
            sleep(0.001)


    def take(self):
        for i in range(1, 101):
            rand_num = randint(50, 500) 
            print(f"Запрос на {rand_num}")
            if rand_num <= self.balance:
                self.balance -= rand_num
                print(f"Снятие: {rand_num}  Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')