#!/usr/bin/python
# coding: utf-8

import requests

r = requests.get('https://github.com/MrTimofeev')
print(r.status_code)

import matplotlib.pyplot as plt
import numpy as np

# Создаем данные
x = np.linspace(0, 10, 100)  # 100 точек от 0 до 10
y = np.sin(x)  # Синус от x

# Создаем график
plt.plot(x, y, label='y = sin(x)', color='blue')

# Добавляем заголовок и метки осей
plt.title('График функции sin(x)')
plt.xlabel('x')
plt.ylabel('y')

# Добавляем легенду
plt.legend()

# Отображаем график
plt.grid()
plt.show()



