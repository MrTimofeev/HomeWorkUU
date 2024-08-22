#!/usr/bin/python
# coding: utf-8

def custom_write(file_name, strings):
    file = open(file=file_name, mode="w", encoding="utf-8")
    result = {}
    for i in strings:
        result.update({(strings.index(i)+1, file.tell()) : i})
        file.write(i + "\n")
        
    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
