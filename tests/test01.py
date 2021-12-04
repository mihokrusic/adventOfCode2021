#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day01
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input01")
        num_input = [int(el) for el in input]
        result = day01.part1(num_input)
        self.assertEqual(result, 7)

    def test_in(self):
        input = inputs.read("input01_actual")
        num_input = [int(el) for el in input]
        result = day01.part1(num_input)
        self.assertEqual(result, 1390)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input01_02")
        num_input = [int(el) for el in input]
        result = day01.part2(num_input)
        self.assertEqual(result, 5)

    def test_in(self):
        input = inputs.read("input01_actual")
        num_input = [int(el) for el in input]
        result = day01.part2(num_input)
        self.assertEqual(result, 1457)

if __name__ == '__main__':
    unittest.main(verbosity=2)