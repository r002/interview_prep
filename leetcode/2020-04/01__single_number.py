# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Notes: Your algorithm should have a linear runtime complexity. Can you implement it without using extra memory?

# Source: https://leetcode.com/problems/single-number

import unittest
from collections import Counter

class Solution:
    def singleNumber(self, nums:list) -> int:
        c = Counter(nums)
        return c.most_common()[-1][0]


class Test(unittest.TestCase):
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]
    s = Solution()

    def test(self):
        for nums, expected in self.cases:
            result = self.s.singleNumber(nums)
            print(f"{nums} | {result} | {expected}")
            self.assertEqual(result, expected)

unittest.main()
