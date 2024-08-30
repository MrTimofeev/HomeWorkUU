#!/usr/bin/python
# coding: utf-8
from datetime import datetime
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, mode="w", encoding="utf-8") as file:
        for i in range(1, word_count):
            sleep(0.1)
            file.write(f"Какое-то слово № {i} \n")
    print(f"Завершилась запись в файл {file_name}")


start1 = datetime.now()
wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")
end1 = datetime.now()
print(f"Работа без потоков: {end1-start1}")

start2 = datetime.now()
thr_first = Thread(target=wite_words, args=(10, "example5.txt"))
thr_second = Thread(target=wite_words, args=(30, "example6.txt"))
thr_third = Thread(target=wite_words, args=(200, "example7.txt"))
thr_fourth = Thread(target=wite_words, args=(100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
end2 = datetime.now()
print(f"Работа с потоками: {end2-start2}")
