#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day04
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input04")
        result = day04.part1(input)
        self.assertEqual(result, 4512)

    def test_in(self):
        input = inputs.read("input04_actual")
        result = day04.part1(input)
        self.assertEqual(result, 50008)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input04")
        result = day04.part2(input)
        self.assertEqual(result, 1924)

    def test_in(self):
        input = inputs.read("input04_actual")
        result = day04.part2(input)
        self.assertEqual(result, 17408)

if __name__ == '__main__':
    unittest.main(verbosity=2)