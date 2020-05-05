import unittest
from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ordered_dict = OrderedDict()
        for index, letter in enumerate(s):
            if letter in ordered_dict:
                ordered_dict[letter].append(index)
            else:
                ordered_dict[letter] = [index]

        for key, val in ordered_dict.items():
            if len(ordered_dict[key])==1:
                return ordered_dict[key][0]  # Return the index

        return -1


class Test(unittest.TestCase):
    t0 = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("", -1),
        ("aaa", -1)
    ]
    s = Solution()

    def test0(self):
        for testcase, expected in self.t0:
            result = self.s.firstUniqChar(testcase)
            print( f"{testcase} | {result} | {expected}")
            self.assertEqual(result, expected)

unittest.main()
