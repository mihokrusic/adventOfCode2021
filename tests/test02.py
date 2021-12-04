#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day02
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input02")
        result = day02.part1(input)
        self.assertEqual(result, 150)

    def test_in(self):
        input = inputs.read("input02_actual")
        result = day02.part1(input)
        self.assertEqual(result, 1660158)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input02")
        result = day02.part2(input)
        self.assertEqual(result, 900)

    def test_in(self):
        input = inputs.read("input02_actual")
        result = day02.part2(input)
        self.assertEqual(result, 1604592846)

if __name__ == '__main__':
    unittest.main(verbosity=2)