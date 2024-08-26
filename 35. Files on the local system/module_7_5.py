#!/usr/bin/python
# coding: utf-8

import os
import datetime

#Совет: при проверке изменить значение переменной directory
directory = "D:\\"

for root, directories, files in os.walk(directory):
    # print(root, directories, files)
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)

        print(f"""Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size}, Время последнего изменения: {datetime.datetime.fromtimestamp(file_time)}, Родительская директория: {parent_dir}""")
        print()
