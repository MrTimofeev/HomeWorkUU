#!/usr/bin/python
# coding: utf-8
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = Runner("Тест1")
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner("Тест2")
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run1 = Runner("Тест3")
        run2 = Runner("Тест4")
        for _ in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1, run2)


if __name__ == "__main__":
    unittest.main()
