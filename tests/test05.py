#!/usr/bin/env python3
import unittest
import os

os.sys.path.insert(0, os.getcwd())

from solutions import day05
from utility import inputs

class Part1(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input05")
        result = day05.part1(input)
        self.assertEqual(result, 5)

    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.part1(input)
        self.assertEqual(result, 4873)

class Part2(unittest.TestCase):
    def test_01(self):
        input = inputs.read("input05")
        result = day05.part2(input)
        self.assertEqual(result, 12)

    def test_in(self):
        input = inputs.read("input05_actual")
        result = day05.part2(input)
        self.assertEqual(result, 19472)

if __name__ == '__main__':
    unittest.main(verbosity=2)