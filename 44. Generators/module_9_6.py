#!/usr/bin/python
# coding: utf-8


def all_variants(text):
    length = len(text)
    result = []
    for start in range(length):
        for end in range(start + 1, length + 1):
            result.append(text[start:end])

    result.sort(key=lambda x: len(x))

    for item in result:
        yield item

a = all_variants("abcd")
for i in a:
    print(i)


"""
Фактически можно было бы не пользоваться созданием списка так как
от этого теряется смысл генератора и его уменьшения затрат памяти,
но я просто не смог придумать как можно сделать вывод такой же как 
и в примере вывода у задачи(((

Не засчитывайте задание если есть более правильное и лаконичное решение
"""