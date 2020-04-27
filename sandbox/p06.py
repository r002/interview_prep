# 1.5 One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

import unittest
import collections

Result = collections.namedtuple("Result", "outcome, message, code")

class SimChecker():
    def __init__(self, l:list):
        self.inputted_pair = l
        self.result = Result(False, "Default Error", "Error00")

        if self.validate(): self.evaluate()
        print(f"{self.result}")


    def evaluate(self):
        word0 = self.inputted_pair[0]
        word1 = self.inputted_pair[1]
        c0 = collections.Counter(word0)
        c1 = collections.Counter(word1)
        i = c0 & c1  # Get the intersection
        r0 = c0 - i
        r1 = c1 - i

        r0_count = sum([item[1] for item in r0.items()])
        r1_count = sum([item[1] for item in r1.items()])

        t0 = r0_count == 0 or r0_count == 1
        t1 = r1_count == 0 or r1_count == 1

        if t0 and t1:
            self.result = Result(True, "w0 and w1 are similar.", "Success")
        else:
            self.result = Result(False, "w0 and w1 aren't similar", "Failure")


    def validate(self)->bool:
        if len(self.inputted_pair) == 2: return True
        self.result = Result(False, "Invalid # of args inputted.", "Error01")
        return False



class Test(unittest.TestCase):
    '''Test Cases'''
    test_cases = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('bale', 'pale', True),
        ('pale', 'bake', False),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test(self):
        for w0, w1, ex_result in self.test_cases:
            test_case = (w0, w1)
            print(f"\n\n{test_case} : {ex_result}")
            actual = SimChecker(test_case).result
            self.assertEqual(actual.outcome, ex_result)

unittest.main()
