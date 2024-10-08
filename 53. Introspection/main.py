#!/usr/bin/python
# coding: utf-8

def introspection_info(obj):
    # Получаем информацию о типе объекта
    obj_type = type(obj).__name__

    atr_and_methods = dir(obj)

    # Фильтруем только атрибуты, исключая методы и встроенные атрибуты
    attributes = [attr for attr in atr_and_methods if not callable(
        getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in atr_and_methods if callable(
        getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = getattr(obj, '__module__', None) if isinstance(
        obj, (type, object)) else None

    # Создаем словарь с собранной информацией
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__

    if hasattr(obj, '__name__'):
        info['name'] = obj.__name__

    return info


# Пример использования функции
if __name__ == "__main__":
    # Создадим пример объекта (класс)
    class Example:
        """Это пример класса."""

        def __init__(self):
            self.attr1 = "attribute 1"
            self.attr2 = "attribute 2"

        def method_one(self):
            pass

        def method_two(self, x):
            return x * 2

    ex = Example()

    # Получаем информацию о объекте
    result = introspection_info(ex)

    # Печатаем результаты
    for key, value in result.items():
        print(f"{key}: {value}")

    # Получаем информацию о объекте
    result = introspection_info("dfsdfs")

    # Печатаем результаты
    for key, value in result.items():
        print(f"{key}: {value}")
