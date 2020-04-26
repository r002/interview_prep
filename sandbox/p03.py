# 1.1 Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?

import unittest
import collections

Result = collections.namedtuple("Result", "passed, message, code")

class UniqueChecker():

    def __init__(self, s:str):
        self.inputted_str = s
        self.valid_str = None
        self.result = Result(passed=False, message="Default Error", code="Error00")

        if self.validate(): self.check_unique()
        print(f"\nOriginal input: {s}")
        print(self.result)

    def validate(self)->bool:
        if len(self.inputted_str) == 0:
            self.result = Result(passed=False, message="Input string is empty", code="Error01")
            return False
        else:
            self.valid_str = self.inputted_str
            return True

    def check_unique(self):
        l = list(self.valid_str)
        if len(l) == len(set(l)):
            self.result = Result(passed=True, message="Str comp is unique", code="Success00")
        else:
            self.result = Result(passed=False, message="Str comp is not unique", code="Failure00")



class Test(unittest.TestCase):
    t00 = "abcd"
    t01 = "abcdd"

    def test00(self):
        actual = UniqueChecker(self.t00).result
        self.assertEqual(True, actual.passed)

    def test01(self):
        actual = UniqueChecker(self.t01).result
        self.assertEqual(False, actual.passed)

unittest.main()
