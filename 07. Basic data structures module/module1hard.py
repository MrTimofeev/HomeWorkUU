#!/usr/bin/python
#coding: utf-8

#Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Сортировка имен студентов по алфавиту
students_sort = sorted(list(students))

#Создание нового словарая где ключ - Имя студента, значение - средний балл
new_dict_student_GPA = {}

#В цикле проходим от 0 до максимального количества студентов
for i in range(0, len(students_sort)):
    # Добавляем в словарь студента и его средний балл
    new_dict_student_GPA.update({students_sort[i]: sum(grades[i])/len(grades[i])})

#Выводим результат
print("Словарь студентов с средним баллом:", new_dict_student_GPA )