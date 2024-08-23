#!/usr/bin/python
# coding: utf-8

class Tournament     ():

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def number_of_participants(self, team1_num=None, team2_num=None):
        # Использование форматирования с помощью
        if team1_num == None and team2_num == None:
            print("Не для одной из команд не были введены количество участников!!!")
            return

        if team1_num != None and team2_num != None:
            print("В команде %s участников: %s!" % (self.team1, team1_num))
            print("В команде %s участников: %s!" % (self.team2, team2_num))
            print("Итого сегодня в командах участников: %s и %s!" %
                  (team1_num, team2_num))
            return

        if team1_num == None or team2_num == None:
            print("Количество участников не задано для: %s" %
                  self.team1 if team1_num == None else self.team2)

    def result_match(self, score_1=None, score_2=None, team1_time=None, team2_time=None):
        # Использование формативарония с помощью format и f строк
        if score_1 == None and score_2 == None:
            print("Не для одной из команд не были введены количество решенных задач!!!")
            return

        if score_1 == None or score_2 == None:
            print("Для одной из команд не были введены количество решенных задач!!!")
            return

        if score_1 != None and score_2 != None:
            print("Команда {} решила задач: {} !".format(self.team1, score_1))
            print("Команда {} решила задач: {} !".format(self.team2, score_2))
            print(f"Команды решили {score_1} и {score_2} задач")

            if team1_time != None and team2_time != None:
                self.time_spent_on_solution(team1_time, team2_time)
            else:
                print("Не для одной команды не введенно время решение задач!!")
                return

            if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
                print(f"Победа команды {self.team1}!")
            elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
                print(f"Победа команды {self.team2}!")
            else:
                print("Ничья")

            print(f"Сегодня было решено {score_1+score_2} задач, в среднем по {(team1_time+team2_time)/(score_1+score_2)} секунды на задачу!.")

    def time_spent_on_solution(self, team1_time, team2_time):
        print("{} решили задачи за {}".format(self.team1, team1_time))
        print("{} решили задачи за {}".format(self.team2, team2_time))


tournament1 = Tournament(team1="Мастера кода", team2="Волшебники данных")

tournament1.number_of_participants(5, 6)
tournament1.result_match(40, 42, 1552.512, 2153.31451)
