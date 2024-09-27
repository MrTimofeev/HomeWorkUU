#!/usr/bin/python
# coding: utf-8
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    # Ошибка заключается в том, что каждый бегун проходит дистанцию мгновенно, 
    # исходя из своей скорости, что может привести к нелогичным результатам. 
    # Следует учитывать время, которое потребуется каждому бегуну для прохождения дистанции. 
    def start(self):
        times = {}
        for participant in self.participants:
            time_to_finish = self.full_distance / participant.speed
            times[participant.name] = time_to_finish

        sorted_finishers = sorted(times.items(), key=lambda x: x[1])
        finishers = {place + 1: name for place,
                     (name, _) in enumerate(sorted_finishers)}
        return finishers


# Класс для тестирования
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Создаём атрибут класса для хранения всех результатов тестов

    def setUp(self):
        # Создаём три объекта: Усэйн (10), Андрей (9), Ник (3)
        self.usain = Runner("Usain", 10)
        self.andrew = Runner("Andrew", 9)
        self.nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        # По завершении всех тестов выводим результаты
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_usain_and_nick(self):
        # Создаём забег на дистанцию 90 с участием Усэйна и Ника
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()

        # Сохраняем результаты теста
        TournamentTest.all_results['test_usain_and_nick'] = results

        # Последний бегун должен быть Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Nick")

    def test_andrew_and_nick(self):
        # Создаём забег на дистанцию 90 с участием Андрея и Ника
        tournament = Tournament(90, self.andrew, self.nick)
        results = tournament.start()

        # Сохраняем результаты теста
        TournamentTest.all_results['test_andrew_and_nick'] = results

        # Последний бегун должен быть Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Nick")

    def test_usain_andrew_nick(self):
        # Создаём забег на дистанцию 90 с участием Усэйна, Андрея и Ника
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        results = tournament.start()

        # Сохраняем результаты теста
        TournamentTest.all_results['test_usain_andrew_nick'] = results

        # Последний бегун должен быть Ник
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Nick")


# Запуск тестов
if __name__ == '__main__':
    unittest.main()
