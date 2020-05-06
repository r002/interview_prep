import time
import unittest
from collections import Counter

# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and
# the majority element always exist in the array.
#
# Source: https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: list) -> int:
        cNums = Counter(nums).most_common(1)
        return cNums[0][0]

    def majorityElement_sort(self, nums: list) -> int:
        nums.sort()
        midpoint_index = len(nums)//2  # Returns third item if len==5 (middle item).
                                       # After sort, middle item is guaranteed to be in majority.
        return nums[midpoint_index]    # Returns fourth item if len==6.
                                       # In fact, third and fourth items
                                       # are guaranteed to be in the majority.

class Test(unittest.TestCase):
    tests = [
        ([1, 1, 2, 2, 2], 2),
        ([1, 1, 2, 2, 3, 3, 3, 3, 3], 3),
        ([1, 2, 1, 2, 1], 1),
        ([1, 2, 1, 2, 2], 2),
        ([1, 1, 1, 2, 2, 2, 2, 2], 2),
        ([1, 1, 1, 1, 1, 2, 2, 2], 1),
        ([1, 2, 3, 5, 5, 5, 5, 5, 6], 5),
        ([1, 2, 1, 2, 2], 2),
        ([3, 3, 4, 4, 4], 4),
        ([3, 3, 4, 4, 5, 5, 5, 5, 5], 5),
        ([3, 4, 3, 4, 3], 3),
        ([3, 4, 3, 4, 4], 4),
        ([1, 1, 1, 2, 2], 1),
        ([1, 1, 2, 2, 2], 2),
        ([1, 1, 2, 3, 3, 3], 3)
    ]

    s = Solution()

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print(f"{self.id()} ({elapsed}s)")

    def test_counter(self):
        for testcase, expected in self.tests:
            result = self.s.majorityElement(testcase)
            print(f"{testcase} | {result} | {expected}")
            self.assertEqual(result, expected)

    def test_sort(self):
        for testcase, expected in self.tests:
            result = self.s.majorityElement_sort(testcase)
            print(f"{testcase} | {result} | {expected}")
            self.assertEqual(result, expected)

unittest.main()
