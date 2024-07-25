#!/usr/bin/python
#coding: utf-8
import random


number = int(random.uniform(3, 20))
result_str = ""
count = 1

while True:
    if count >= number-count:
        break


    for i in range(2,number):
        if number % (count + i) == 0 and (count + i) != (count + (number -count)) and count < i:
            result_str = result_str + str(count) + str(i)


    if number > count:
        result_str = result_str + str(count) + str(number-count)
        
    count += 1
    

print(number, "-", result_str) 

