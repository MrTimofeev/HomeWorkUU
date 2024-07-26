#!/usr/bin/python
#coding: utf-8

calls = 0 

def count_calls():
    global calls
    calls += 1
    return

def string_info(string_):
    count_calls()
    len_string = len(string_)
    upper_string = string_.upper()
    lower_string = string_.lower()
    return (len_string, upper_string, lower_string)


def is_contains(string_, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()

    if string_.lower() in list_to_search:
        return True
    else:
        return False 


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(calls)

