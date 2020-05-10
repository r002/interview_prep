import unittest

# Assumptions:
# 1. nums is guaranteed to be non-empty.

# Sources:
# https://leetcode.com/problems/maximum-subarray
# https://en.wikipedia.org/wiki/Maximum_subarray_problem

class Solution:
    def maxSubArray(self, nums:list) -> int:
        zero_is_possible = False

        # Run Kadane's algorithm:
        best_sum = 0
        current_sum = best_sum
        for x in nums:
            current_sum = max(0, current_sum + x)
            best_sum = max(best_sum, current_sum)
            # print(f"x: {x}\t| current_sum: {current_sum} | best_sum: {best_sum}")

            if x==0: zero_is_possible = True

        # If best_sum is 0, confirm edgecase that nums aren't all negative.
        # If nums ARE all negative, there needs to at least be a zero in nums.
        if 0==best_sum and not zero_is_possible:
            return max(nums)  # In this case, best_sum will be the smallest negative num in nums.

        return best_sum


class Test(unittest.TestCase):
    cases = [
        ([0, -1], 0),
        ([-3, -2, -1, 0], 0),
        ([-3, -2, -1, 1], 1),
        ([-3, -2, -1], -1),  # All negatives.
        ([99], 99),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    ]
    s = Solution()

    def test0(self):
        for nums, expected in self.cases:
            result = self.s.maxSubArray(nums)
            print(f"{nums} | {result} | {expected}")
            self.assertEqual(result, expected)

unittest.main()
