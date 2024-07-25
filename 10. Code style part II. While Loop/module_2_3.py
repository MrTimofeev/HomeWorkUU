#!/usr/bin/python
#coding: utf-8

my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

x = 0
while True:
    if x == len(my_list):
        break
    elif my_list[x] < 0:
        break
    elif my_list[x] != 0:
        print(my_list[x])
    x += 1

