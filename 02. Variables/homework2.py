#!/usr/bin/python
#coding: utf-8

count_complete_DZ = 12
count_of_house_spent = 1.5
name_course = 'Python'
time_to_task = count_of_house_spent/count_complete_DZ

# Первый способ вывода
print('Курс:', name_course,', всего задач:', count_complete_DZ, ', затрачено часов:', count_of_house_spent, ', среднее время выполнения ', time_to_task, 'часа.')
# Второй способ вывода
print(f'Курс: {name_course}, всего задач:{count_complete_DZ}, затрачено часов: {count_of_house_spent}, среднее время выполнения {time_to_task} часа.')

