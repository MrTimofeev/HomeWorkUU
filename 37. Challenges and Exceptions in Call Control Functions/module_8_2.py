#!/usr/bin/python
# coding: utf-8

class calculate():
    def personal_sum(self, numbers):
        sum_ = 0
        incorrect_data = 0
        for i in numbers:
            try:
                sum_ += i
            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы {i}")

        return (sum_, incorrect_data)

    def calculate_average(self, numbers):
        try:
            result_sum, result_incorrect_data = self.personal_sum(numbers)
            result = result_sum / (len(numbers) - result_incorrect_data) 
            print(f"Результат: {result}" )
            return result
        except ZeroDivisionError:
            print("Результат: 0" )
            return 0
        except TypeError:
            print("В numbers записан некорректный тип данных")
            return None


Calculator = calculate()

Calculator.calculate_average("1, 2, 3")
Calculator.calculate_average([1, "Строка", 3, "Ещё Строка"])
Calculator.calculate_average(567)
Calculator.calculate_average([42, 15, 36, 13])
