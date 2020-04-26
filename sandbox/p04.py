# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

import unittest
import collections

Result = collections.namedtuple("Result", "outcome, message, code")

def convert_to_ascii(s:str)->list:
    return [ord(_) for _ in s]

class CheckPerm():
    def __init__(self, l:list):
        self.inputted_pair = l
        self.result = Result(False, "Default Failure Message", "Error00")

        if self.validate(): self.evaluate()
        print(f"\n\nOriginal input: {l}")
        print(self.result)

    def validate(self)->bool:
        if len(self.inputted_pair) != 2:
            self.result = Result(False, "Input args wrong number! Two expected.", "Error01")
            return False

        if (type(self.inputted_pair[0]) != str or type(self.inputted_pair[1]) != str):
            self.result = Result(False, "Input args wrong type! Str expected.", "Error02")
            return False

        return True

    def evaluate(self):
        asci_rep0 = convert_to_ascii(self.inputted_pair[0])
        asci_rep1 = convert_to_ascii(self.inputted_pair[1])
        asci_rep0.sort()
        asci_rep1.sort()

        if(asci_rep0==asci_rep1):
            self.result = Result(True, "Strings are perms.", "Success")
        else:
            self.result = Result(False, "Strings aren't perms.", "Failure")

class Test(unittest.TestCase):
    t00 = ["abc", "bca"]
    t01 = []
    t02 = [123, 456]
    t03 = ["aaa", "bbb"]

    def test00(self):
        actual = CheckPerm(self.t00).result
        self.assertEqual(True, actual.outcome)

    def test01(self):
        actual = CheckPerm(self.t01).result
        self.assertEqual(False, actual.outcome)

    def test02(self):
        actual = CheckPerm(self.t02).result
        self.assertEqual(False, actual.outcome)

    def test03(self):
        actual = CheckPerm(self.t03).result
        self.assertEqual(False, actual.outcome)


unittest.main()
