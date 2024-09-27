#!/usr/bin/python
# coding: utf-8
import unittest
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest


All_tests = unittest.TestSuite()

All_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
All_tests.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(All_tests)
